import requests
from bs4 import BeautifulSoup

quote_webpage = requests.get('https://www.goodreads.com/quotes')
soup = BeautifulSoup(quote_webpage.text, 'html.parser')
quotes = soup.find_all(class_ = 'quoteDetails')

for quote in quotes:
    quoteText = quote.find(class_ = 'quoteText')
    author = quoteText.span.extract().get_text().strip()
    quote_text = quoteText.get_text().strip().split('―')[0]
    print ("Author: ", author)
    print ("Quote_text: ", quote_text)