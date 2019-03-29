import os
from flask import Flask, jsonify, request
from db import db
import quotesdb

from models.quote import QuoteModel
from controllers.quote import QuoteController
from views.quote import QuoteView

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///webquotes.db')

@app.route('/', methods=['GET'])
def home():
    return "This shit gets quotes"
 
# Takes theme and author parameters and returns random quote with related theme and author
@app.route('/searchQuote/<string:theme>/<string:author>', methods = ['GET'])
def search_quote(theme, author):
    return QuoteView.get_quote(theme, author)

@app.route('/enterQuote/<string:theme>/<string:author>/<string:quote>', methods = ['POST'])
def enter_quote(theme, author, quote):
    return QuoteView.enter_quote(theme, author, quote)

if __name__ == '__main__':
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(debug = True)