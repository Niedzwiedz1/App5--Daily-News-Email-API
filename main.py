import requests

from functions import send_email

api_key = "39e5143b5e4d45ef8c515696c51c14bb"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
        "2023-11-19&sortBy=publishedAt&apiKey=39e5143b5e4d45ef8c515696c51c14bb"

request = requests.get(url)
content = request.json()
e_mail = f"""\
Subject: Daily News

\n

"""
for article in content["articles"]:
    title = article["title"]
    url = article["url"]
    news = f"{title} \n {url} \n\n"
    e_mail = e_mail + news

e_mail = e_mail.encode("utf-8")
mail = send_email(message=e_mail)


