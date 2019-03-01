import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
import unittest
import tempfile
from app import app
from db import db
import json

TEST_DB = 'quotes.db'

list_of_quotes = ['Love is great', 'Fuck you', 'Slavery sucks', 'Code as clean as my room',
                  'SEX', 'Money brings happiness', 'Here he is at 19 getting laid', 'Black people have big dicks']

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///quotes.db')
        self.app = app.test_client()
        db.init_app(app)
        # db.drop_all(app=app)
        db.create_all(app=app)

    def tearDown(self):
        pass

    def test_no_quotes(self):
        get_quote = self.app.get('/api/allCategorySearch/Life/Bob')
        self.assertEqual (get_quote.status_code, 204)

    def test_get_quotes(self):
        get_quote = self.app.get('/api/allCategorySearch/Life/Lincoln')
        self.assertEqual (get_quote.status_code, 200)
        data_get_quote = json.loads(get_quote.data.decode())
        self.assertEqual(len(data_get_quote), 1)
        self.assertEqual(len(data_get_quote['response']), 4)
        self.assertEqual(data_get_quote['response']['quote'] in list_of_quotes, True)
        self.assertEqual(data_get_quote['response']['quote'], 'Slavery sucks')


if __name__ == '__main__':
    unittest.main()