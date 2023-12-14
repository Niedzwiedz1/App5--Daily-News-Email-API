import requests

api_key = "39e5143b5e4d45ef8c515696c51c14bb"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-14&sortBy" \
      "=publishedAt&apiKey=39e5143b5e4d45ef8c515696c51c14bb"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    title = article["title"]
    print(title)
