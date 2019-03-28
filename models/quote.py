from db import db

class QuoteModel(db.Model):
    __tablename__ = 'quotesList'

    id = db.Column(db.Integer, primary_key=True)
    quote = db.Column(db.String(255))
    theme = db.Column(db.String(255))
    author = db.Column(db.String(255))

    def __init__(self, quote, theme, author):
        self.quote = quote
        self.theme = theme
        self.author = author

    def json(self):
        return {
            "id": self.id,
            "quote": self.quote,
            "theme": self.theme,
            "author": self.author
        }

    @classmethod
    def find_by_category(cls, theme, author):
        return cls.query.filter_by(theme=theme, author = author).all()