import streamlit as st
import requests

# prepare api key an url
api_key = "KrgMgDkyF9wW7isYvnCBZIE2FSYlaRKIrgzeBEzp"
url = ("https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")


# get the request data as dictionary
response1 = requests.get(url)
data = response1.json()

# extract the image title , url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# download the image
image_path = "img.png"
response2 = requests.get(image_url)
with open(image_path, "wb") as file:
    file.write(response2.content)

st.title(title)
st.image(image_path)
st.write(explanation)

