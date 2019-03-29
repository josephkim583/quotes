from flask import request
from flask.views import MethodView
from random import randint
from controllers.quote import QuoteController
import json

class QuoteView(MethodView):

    req_params = ['theme', 'author']

    @classmethod
    def get_quote(cls, theme, author):
        error_message, status, response = QuoteController.get_quote(theme, author)

        if error_message:
            return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": response}), status   

    @classmethod
    def enter_quote(cls, theme, author, quote):
        # error_message, status, response = QuoteController.enter_quote(theme, author, quote)

        # if error_message:
        #     return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": 'Success!'})
