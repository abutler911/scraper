import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random

# === Config ===
BASE_URL = "http://quotes.toscrape.com/page/{}/"
BASE_DOMAIN = "http://quotes.toscrape.com"
CSV_FILE = "quotes.csv"
JSON_FILE = "quotes.json"
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Linux x86_64)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)",
]

# === Prepare Output Files ===
with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Quote", "Author", "Tags", "Born Date", "Born Location", "Bio"])

all_data = []

# === Main Scraper Loop ===
page = 1
while True:
    headers = {"User-Agent": random.choice(USER_AGENTS)}
    url = BASE_URL.format(page)
    print(f"\n📄 Scraping page {page}: {url}")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    quotes = soup.select(".quote")

    if not quotes:
        print("✅ No more quotes found. Done.")
        break

    for quote in quotes:
        text = quote.select_one(".text").get_text(strip=True)
        author = quote.select_one(".author").get_text(strip=True)
        tags = ", ".join(tag.get_text(strip=True) for tag in quote.select(".tags .tag"))
        author_url = BASE_DOMAIN + quote.select_one("a")["href"]

        # Get author details
        author_response = requests.get(author_url, headers=headers)
        author_soup = BeautifulSoup(author_response.text, "lxml")
        born_date = author_soup.select_one(".author-born-date").get_text(strip=True)
        born_location = author_soup.select_one(".author-born-location").get_text(strip=True)
        bio = author_soup.select_one(".author-description").get_text(strip=True)

        # Save to CSV
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([text, author, tags, born_date, born_location, bio])

        # Save to memory for JSON
        all_data.append({
            "quote": text,
            "author": author,
            "tags": tags.split(", "),
            "born_date": born_date,
            "born_location": born_location,
            "bio": bio
        })

        print(f"💬 \"{text}\" — {author}")
        print(f"📌 Tags: {tags}")
        print(f"📚 Bio: Born {born_date} in {born_location}")

    page += 1
    time.sleep(1)

# === Export JSON ===
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Scraping complete! Data saved to {CSV_FILE} and {JSON_FILE}")
