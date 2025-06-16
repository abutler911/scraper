# 🧠 Quotes Dashboard Scraper (Flask + Bootstrap)

This project scrapes inspirational quotes from [quotes.toscrape.com](http://quotes.toscrape.com), extracts the quote text, authors, tags, and author bios, and displays them in a beautiful, searchable dashboard built with Flask and Bootstrap.

---

## 🚀 Features

- 🔁 Scrapes all pages with pagination
- ✍️ Extracts quotes, authors, tags, birth date/location, and bio
- 💾 Saves data to both CSV and JSON
- 🕵️‍♂️ Rotates User-Agent headers
- 💤 Throttles requests to avoid server blocks
- 🧭 Responsive, dark-themed dashboard
- 🎲 Random Quote generator
- 🔍 Searchable by quote text, author, or tag

---

## 🧱 Project Structure

scraper/
├── app.py # Flask app
├── scrape.py # Web scraper script
├── quotes.json # Scraped data in JSON
├── quotes.csv # Scraped data in CSV
├── requirements.txt # Python dependencies
├── render.yaml # Render deployment config
├── templates/
│ ├── index.html # Dashboard view
│ └── random.html # Random quote view
├── .gitignore
└── README.md

---

## 💻 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/flask-scraper.git
cd flask-scraper

2. Set up a virtual environment

python -m venv venv
source venv/Scripts/activate  # Windows
or: source venv/bin/activate  # macOS/Linux

3. Install dependencies

pip install -r requirements.txt

4. Run the scraper

python scrape.py

5. Start the web app

python app.py

Visit http://localhost:5000 in your browser.
🌐 Deployment on Render

    Push this project to GitHub.

    Go to https://render.com and create a new Web Service.

    Use the following settings:

        Build Command: (leave blank)

        Start Command: gunicorn app:app

        Environment: Python

    Make sure requirements.txt and render.yaml are in your repo.
```
