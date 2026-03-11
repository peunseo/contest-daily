import requests
from bs4 import BeautifulSoup
import json

url = "https://www.wevity.com/?c=find&s=1&gub=1"

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

contests = []

for item in soup.select("li.list"):
    title_tag = item.select_one(".tit")
    link_tag = item.select_one("a")

    if title_tag and link_tag:
        title = title_tag.text.strip()
        link = "https://www.wevity.com" + link_tag["href"]

        contests.append({
            "title": title,
            "link": link
        })

with open("contests.json","w",encoding="utf-8") as f:
    json.dump(contests,f,ensure_ascii=False,indent=2)
