from db import db

class BookmarkModel(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    article_url = db.Column(db.String, nullable=False)
    summary = db.Column(db.String, nullable=False)