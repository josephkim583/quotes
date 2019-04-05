import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
basedir = os.path.abspath(os.path.dirname(__file__))
import unittest
import tempfile
from app import app
from db import db
import json

TEST_DB = 'webquotes.db'

class BasicTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///webquotes.db')
        self.app = app.test_client()
        db.init_app(app)
        # db.drop_all(app=app)
        db.create_all(app=app)

    def tearDown(self):
        pass

    def test_no_quotes(self):
        get_quote = self.app.get('/searchQuote/Life/Fuck')
        data_get_quote = json.loads(get_quote.data.decode())
        self.assertEqual (get_quote.status_code, 200)
        self.assertEqual (data_get_quote['response'], 'No quotes were found')

    def test_get_quotes(self):
        get_quote = self.app.get('/searchQuote/Life/Joseph')
        self.assertEqual (get_quote.status_code, 200)
        data_get_quote = json.loads(get_quote.data.decode())
        self.assertEqual(data_get_quote['response']['quote'], 'WTF')

    def test_make_quote(self):
        new_quote= self.app.post('/enterQuote', data= {
                                        "theme": "Life",
                                        "author": "Mark",
                                        "quote": "My code as clean as my room"
                                    }
                                )
        self.assertEqual(new_quote.status_code, 201)

    def test_make_wrong_quote(self):
        new_quote= self.app.post('/enterQuote', data= {
                                        "theme": "Life",
                                        "author": "Mark",
                                    }
                                )
        self.assertEqual(new_quote.status_code, 400)

if __name__ == '__main__':
    unittest.main()