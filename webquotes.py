import requests
from bs4 import BeautifulSoup

quote_webpage = requests.get('https://www.goodreads.com/quotes')
soup = BeautifulSoup(quote_webpage.text, 'html.parser')
quotes = soup.find_all(class_ = 'quoteText')

quote = soup.find(class_= 'quoteText')


for quote in quotes:
    author = quote.span.extract().get_text()
    quote_text = quote.get_text().strip()[:-1]
    print ("Author: ", author)
    print ("Quote_text: ", quote_text)