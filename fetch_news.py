"""
Fetch a fresh batch of English news articles once a week and save them
to data/articles.json, which the app reads.

Requires a free API key from https://newsapi.org/register
(no credit card needed), stored as the GitHub secret NEWS_API_KEY.
"""
import os
import json
import datetime
import urllib.request
import urllib.parse
import urllib.error

API_KEY = os.environ.get("NEWS_API_KEY")
if not API_KEY:
    raise SystemExit("Missing NEWS_API_KEY environment variable / secret.")

# Rotates the topic each week so the app doesn't always show the same category.
CATEGORIES = ["science", "technology", "health", "general", "business"]
today = datetime.date.today()
category = CATEGORIES[today.isocalendar()[1] % len(CATEGORIES)]

params = {
    "language": "en",
    "category": category,
    "pageSize": 15,
    "apiKey": API_KEY,
}
url = "https://newsapi.org/v2/top-headlines?" + urllib.parse.urlencode(params)

try:
    with urllib.request.urlopen(url, timeout=20) as resp:
        data = json.load(resp)
except urllib.error.HTTPError as e:
    raise SystemExit(f"NewsAPI request failed: {e.code} {e.read().decode(errors='ignore')}")

articles = []
for a in data.get("articles", []):
    title = (a.get("title") or "").strip()
    description = (a.get("description") or "").strip()
    source = (a.get("source") or {}).get("name", "")
    link = a.get("url", "")
    published = a.get("publishedAt", "")
    if not title or not description or not link:
        continue
    # Skip low quality "[Removed]" entries NewsAPI sometimes returns
    if "[Removed]" in title or "[Removed]" in description:
        continue
    words = len(description.split())
    articles.append({
        "title": title,
        "description": description,
        "source": source,
        "url": link,
        "publishedAt": published,
        "category": category,
        "readMinutes": max(1, round(words / 130)),
    })

out = {
    "updated": today.isoformat(),
    "week": today.isocalendar()[1],
    "category": category,
    "articles": articles[:15],
}

os.makedirs("data", exist_ok=True)
with open("data/articles.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"Saved {len(out['articles'])} articles for category '{category}' (week {out['week']})")
