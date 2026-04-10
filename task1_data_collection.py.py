import requests
import time
import json
import os
from datetime import datetime
headers = {"User-Agent": "TrendPulse/1.0"}


categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


def get_category(title):
    title = title.lower()
    for cat, words in categories.items():
        for w in words:
            if w in title:
                return cat
    return None

url = "https://hacker-news.firebaseio.com/v0/topstories.json"

try:
    res = requests.get(url, headers=headers)
    story_ids = res.json()[:500]
except:
    print("Failed to fetch story IDs")
    story_ids = []

collected_data = []
category_count = {c: 0 for c in categories}


for category in categories:
    for sid in story_ids:

        if category_count[category] >= 25:
            break

        try:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{sid}.json"
            r = requests.get(story_url, headers=headers)
            data = r.json()

            if not data or "title" not in data:
                continue

            cat = get_category(data["title"])

            if cat == category:
                record = {
                    "post_id": data.get("id"),
                    "title": data.get("title"),
                    "category": cat,
                    "score": data.get("score"),
                    "num_comments": data.get("descendants", 0),
                    "author": data.get("by"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

                collected_data.append(record)
                category_count[category] += 1

        except:
            print(f"Error fetching story {sid}")
            continue

    time.sleep(2)


if not os.path.exists("data"):
    os.makedirs("data")

filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

with open(filename, "w") as f:
    json.dump(collected_data, f, indent=4)

print(f"Collected {len(collected_data)} stories. Saved to {filename}")
