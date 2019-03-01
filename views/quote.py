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
        if len(response) == 0:
            return json.dumps({"response": None}), status
        index = randint(0, (len(response) - 1))
        return json.dumps({"response": response[index].json()}), status
