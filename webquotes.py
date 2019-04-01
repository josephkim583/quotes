import requests
from bs4 import BeautifulSoup

quote_webpage = requests.get('https://www.goodreads.com/quotes')
soup = BeautifulSoup(quote_webpage.text, 'html.parser')
quotes = soup.find_all(class_ = 'quoteDetails')

for quote in quotes:
    quoteFooter = quote.find(class_ = 'quoteFooter')
    quoteText = quote.find(class_ = 'quoteText')
    theme = quoteFooter.find("a").get_text()
    author = quoteText.span.extract().get_text().strip()
    quote_text = quoteText.get_text().strip().split('―')[0]

    requests.post("http://localhost:5000/enterQuote", data = {"theme": theme, "author": author, "quote": quote_text})

    print ("Author: ", author)
    print ("Quote_text: ", quote_text)
    print ("Theme: ", theme)

