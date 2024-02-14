from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# now we need to connect html pages with that website object

# always give another / after a path

# for home page

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home():
    return render_template("home.html",
                           data=stations.to_html())  # to render html document whenever user visits website url
    # "/home"
    # also we use .to_html() to present the data on webpage as rows and columns/ table ,
    # for that we also need to add <p>{{data|safe}}</p> instead of just <p>{{data}}</p> in body of html code


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    # because data starts from row 20 we use skiprows
    # The zfill will add the zeros in-front , to match the format of the file naminf

    return {"station": station,
            "date": date,
            "temperature": temperature}  # to render html document whenever user visits website url "/home"


@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient="records")  # orient = records is used to reformat the data as date, tg, etc in one pair
    return result


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station,year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)  # we removed the parse_date to change is type back to norma from date time type
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient="records")
    return result



# but for that we need that html file in templates folder

if __name__ == "__main__":
    app.run(debug=True)
