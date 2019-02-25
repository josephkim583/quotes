from flask import request
from flask.views import MethodView
# from util.parser import ReqParser
from controllers.quote import QuoteController
import json

class QuoteView(MethodView):

    req_params = ['theme', 'category']

    @classmethod
    def get_quote(cls, theme, category):
        error_message, status, response = QuoteController.get_quote(theme, category)

        if error_message:
            return json.dumps({"error_message": error_message}), status

        return json.dumps({"response": response.json()}), status



     @classmethod
    def get_accord(cls, name):
        error_message, status, response = AccordController.get_accord(name)

        if error_message:
            return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": response.json()}), status
