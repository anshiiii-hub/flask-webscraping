#importing libraries
from flask import Flask,render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/scrape')
def scrape():
    url = 'https://books.toscrape.com/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find_all('article', class_='product_pod')
    books = []
    for item in data:
        title = item.find('h3').find('a')['title']
        price = item.find('p', class_='price_color').get_text(strip=True)
        availability = item.find('p', class_='instock availability').get_text(strip=True)
        books.append({'title': title, 'price': price, 'availability': availability})
        df = pd.DataFrame(books)

    return render_template('index.html', books=df.to_html(classes='table table-striped', index=False))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0',port=5000)