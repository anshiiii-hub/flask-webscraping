# flask-webscraping

A minimal Flask app that scrapes a practice bookstore ([books.toscrape.com](https://books.toscrape.com/)) and displays the books in a table. An early step in my web-scraping learning, and a close sibling of [`web-scraping`](https://github.com/anshiiii-hub/web-scraping).

## What it does

- `/` is the home page.
- `/scrape` fetches the bookstore's front page, reads each book's **title**, **price** and **availability**, puts them in a pandas DataFrame, and renders them as a striped HTML table.

## Tech

Python · Flask · requests · BeautifulSoup (`bs4`) · pandas

## Run it locally

```bash
git clone https://github.com/anshiiii-hub/flask-webscraping.git
cd flask-webscraping
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000 and follow the link to `/scrape`.

## Notes

The target site is a sandbox built for scraping practice. This is a learning project: it only reads the first page of results.
