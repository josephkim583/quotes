from models.quote import QuoteModel

class QuoteController():

    @classmethod
    def get_quote(cls, theme, author):
        try:
            target_quote = QuoteModel.find_by_category(theme, author)
        except:
            return "Internal System Error", 500, None
        return "", 200, target_quote

