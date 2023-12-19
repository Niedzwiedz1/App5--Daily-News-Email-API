import requests

from functions import send_email

topic = "tesla"
api_key = "39e5143b5e4d45ef8c515696c51c14bb"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-11-19&" \
      "sortBy=publishedAt&" \
      "apiKey=39e5143b5e4d45ef8c515696c51c14bb&language=en"

request = requests.get(url)
content = request.json()
e_mail = "Subject: Daily News \n"

for article in content["articles"][:11]:
    title = article["title"]
    url = article["url"]
    news = f"{title} \n {url} \n\n"
    e_mail = e_mail + news

e_mail = e_mail.encode("utf-8")
mail = send_email(message=e_mail)


