import requests
from bs4 import BeautifulSoup
import json

url = "https://www.linkareer.com/contest"  # 예시 URL
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

contests = []

for item in soup.select(".contest-item"):  # 실제 클래스명은 확인 필요
    title = item.select_one(".contest-title").text.strip()
    link = item.select_one("a")["href"]
    contests.append({
        "title": title,
        "link": link
    })

with open("contests.json", "w", encoding="utf-8") as f:
    json.dump(contests, f, ensure_ascii=False, indent=2)
