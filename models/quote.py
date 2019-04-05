from db import db
from models.common import CommonModel

class QuoteModel(db.Model, CommonModel):
    __tablename__ = 'webquotes'

    quote = db.Column(db.String(255), primary_key=True)
    theme = db.Column(db.String(255))
    author = db.Column(db.String(255))

    def __init__(self, quote, theme, author):
        self.quote = quote
        self.theme = theme
        self.author = author

    def json(self):
        return {
            "quote": self.quote,
            "theme": self.theme,
            "author": self.author
        }

    @classmethod
    def find_by_category(cls, theme, author):
        return cls.query.filter_by(theme=theme, author = author).all()
