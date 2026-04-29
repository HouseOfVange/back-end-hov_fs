from sqlalchemy.orm import backref
from app import db

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    #likes_count = db.Column(db.Integer)
    piece_id = db.Column(db.Integer, db.ForeignKey('piece.piece_id', ondelete='cascade'))