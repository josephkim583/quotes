from flask import Flask, jsonify, request
import quotesdb

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "This shit gets quotes"

'''
I left two approaches of doing it. I think the second approach is the smarter choice, especially as I start adding more categories.
I was also wondering what the pros and cons of each approach and when I should be using them. 
'''    

'''Approach 1'''
# Takes no parameters and returns random quote
@app.route('/api/generalSearch', methods=['GET'])
def general_search_quote():
    return quotesdb.read_from_db("None", "None") 

# Takes theme parameter and returns random quote with related theme
@app.route('/api/themeSearch/<theme>', methods = ['GET'])
def theme_search_quote(theme):
    return quotesdb.read_from_db(theme, "None")

# Takes author parameter and returns random quote with related author
@app.route('/api/authorSearch/<author>', methods = ['GET'])
def author_search_quote(author):
    return quotesdb.read_from_db("None", author)

# Takes theme and author parameters and returns random quote with related theme and author
@app.route('/api/allCategorySearch/<theme>/<author>', methods = ['GET'])
def category_search_quote(theme, author):
    return quotesdb.read_from_db(theme, author)


'''Approach 2'''
# Takes in theme and author arguments. If not provided, then are defaulted to None
@app.route('/api/categorySearch', methods = ['GET'])
def category_quote():
    theme = author = None
    if 'theme' in request.args:
        theme = request.args['theme']
    if 'author' in request.args:
        author = request.args['author']
    return quotesdb.read_from_db(theme, author)

if __name__ == '__main__':
    app.run(debug = True)