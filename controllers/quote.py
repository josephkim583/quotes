from models.quote import QuoteModel
from random import randint
import json

class QuoteController():

    @classmethod
    def get_quote(cls, theme, author):
        try:
            target_quote = QuoteModel.find_by_category(theme, author)
            if len(target_quote) == 0:
                return "", 200, None
            else:
                index = randint(0, (len(target_quote) - 1))
                quote = target_quote[index]
        except:
            return "Internal System Error", 500, None
        return "", 200, quote.json()

