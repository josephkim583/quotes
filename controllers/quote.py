from models.quote import QuoteModel
from random import randint
import json

class QuoteController():

    @classmethod
    def get_quote(cls, theme, author):
        try:
            target_quote = QuoteModel.find_by_category(theme, author)
            if len(target_quote) == 0:
                return "", 200, "No quotes were found"
            else:
                index = randint(0, (len(target_quote) - 1))
                quote = target_quote[index]
        except:
            return "Internal System Error", 500, None
        return "", 200, quote.json()

    @classmethod
    def enter_quote(cls, data):
        try:
            new_quote = QuoteModel(data["theme"], data["author"], data["quote"])
            new_quote.save_to_db()
        except:
            return "Internal Server Error", 500, None

        return "", 201, None