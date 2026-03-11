import requests
from bs4 import BeautifulSoup
import json

url = "https://www.linkareer.com/contest"  # 실제 URL 확인 필요
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")

contests = []

# 실제 HTML 구조에 맞는 selector 사용
for item in soup.select(".contest-list-item"):  
    title_tag = item.select_one(".contest-title")
    link_tag = item.select_one("a")
    if title_tag and link_tag:
        contests.append({
            "title": title_tag.text.strip(),
            "link": link_tag["href"]
        })

with open("contests.json", "w", encoding="utf-8") as f:
    json.dump(contests, f, ensure_ascii=False, indent=2)
