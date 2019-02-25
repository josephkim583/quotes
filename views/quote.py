from flask import request
from flask.views import MethodView
# from util.parser import ReqParser
from controllers.quote import QuoteController
import json

class QuoteView(MethodView):

    req_params = ['theme', 'author']

    @classmethod
    def get_quote(cls, theme, author):
        error_message, status, response = QuoteController.get_quote(theme, author)
        if error_message:
            return json.dumps({"error_message": error_message}), status

        return json.dumps({"response": list(map(lambda x : x.json() if x else None, response))}), status
