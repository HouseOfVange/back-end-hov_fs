from sqlalchemy.orm import backref
from app import db
from datetime import datetime, timezone


class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    piece_id = db.Column(db.Integer, db.ForeignKey('piece.piece_id', ondelete='cascade'))

    def to_dict(self):
        return {
            "id": self.comment_id,
            "author": self.author,
            "message": self.message,
            "likes_count": self.likes_count,
            "created_at": self.created_at,
            "piece_id": self.piece_id
        }
    