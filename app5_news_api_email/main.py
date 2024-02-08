import requests  # this is used to get content from url / brwose an api

api_key = "305cd13bea2348398dadfc5bc316e02d"
url = "https://newsapi.org/v2/everything?q=tesla&" \
       "from=2024-01-08&sortBy=publishedAt&apiKey=" \
       "305cd13bea2348398dadfc5bc316e02d"

request = requests.get(url)
content = request.json()  # gets content from that url in json format
for article in content["articles"]:
       print(article["title"])
       print(article["description"])

