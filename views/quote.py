from flask import request
from flask.views import MethodView
from util.parser import ReqParser
from random import randint
from controllers.quote import QuoteController
import json

class QuoteView(MethodView):

    req_params = ['theme', 'author', 'quote']

    @classmethod
    def get_quote(cls, theme, author):
        error_message, status, response = QuoteController.get_quote(theme, author)

        if error_message:
            return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": response}), status   

    @classmethod
    def enter_quote(cls):
        data = request.form
        if not ReqParser.check_body(data, cls.req_params):
            return json.dumps({"response": "ill-formed request"}), 400

        error_message, status, response = QuoteController.enter_quote(data)

        if error_message:
            return json.dumps({"error_message": error_message}), status
        return json.dumps({"response": 'Success!'}), status
