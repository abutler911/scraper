from flask import Flask, render_template, request
import json
import random

app = Flask(__name__)

# Load quotes from JSON
with open("quotes.json", "r", encoding="utf-8") as f:
    QUOTES = json.load(f)

@app.route("/")
def index():
    query = request.args.get("q", "").lower()
    filtered_quotes = []

    for q in QUOTES:
        if (query in q["quote"].lower() or
            query in q["author"].lower() or
            any(query in tag.lower() for tag in q["tags"])):
            filtered_quotes.append(q)

    return render_template("index.html", quotes=filtered_quotes if query else QUOTES, query=query)

@app.route("/random")
def random_quote():
    quote = random.choice(QUOTES)
    return render_template("random.html", quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
