import requests  # this is used to get content from url / brwose an api
from send_email import send_email

api_key = "305cd13bea2348398dadfc5bc316e02d"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-01-08&sortBy=publishedAt&apiKey=" \
      "305cd13bea2348398dadfc5bc316e02d"

# Make request
request = requests.get(url)

# Get the dictionary with data
content = request.json()  # gets content from that url in json format

# Access the article titles and description
body = ""
for article in content["articles"]:
    body = body + str(article["title"]) + "\n" + str(article["description"]) + 2*"\n"

body=body.encode("utf-8")  # need to convert the body into this format before we send mail, else it throws error
send_email(message=body)
