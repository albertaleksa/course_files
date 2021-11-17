import requests
from bs4 import BeautifulSoup
from csv import DictWriter
import time

response = requests.get("https://www.kxan.com/")
soup = BeautifulSoup(response.text, "html.parser")
articles = soup.find_all("article", class_="article-list__article--is-slat")
print(len(articles))
print()
print()

with open("news_data.csv", "w") as file:
    headers = ["title", "url", "date"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()

    for article in articles:
        # print(article.prettify())
        a_tag = article.find("a")
        title = a_tag.get_text(strip=True)
        url = a_tag["href"]
        raw_time_article = article.find("time")["datetime"] if article.find("time") else None
        if raw_time_article:
            str_time = time.strptime(raw_time_article, "%Y-%m-%dT%H:%M:%S-06:00")
            date = time.strftime("%Y-%m-%d %H:%M:%S", str_time)
        else:
            date = ""
        csv_writer.writerow({
            "title": title,
            "url": url,
            "date": date
        })

