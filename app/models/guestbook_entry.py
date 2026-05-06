from app import db
from datetime import datetime, timezone


class GuestbookEntry(db.Model):
    entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    message = db.Column(db.String, nullable=False)
    likes_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    def to_dict(self):
        return {
            "id": self.entry_id,
            "author": self.author,
            "message": self.message,
            "likes_count": self.likes_count,
            "created_at": self.created_at
        }
    