from app import db

class Piece(db.Model):
    piece_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    client = db.Column(db.String)
    piece_description = db.Column(db.String)
    order_year = db.Column(db.Integer)
    delivery_year = db.Column(db.Integer)
    image_url = db.Column(db.String)
    is_available = db.Column(db.Boolean)

    comment = db.relationship("Comment", backref="piece", passive_deletes=True)

    def to_dict(self):
        return {
            "id": self.piece_id,
            "title": self.title,
            "client": self.client,
            "description": self.piece_description,
            "order_year": self.order_year,
            "delivery_year": self.delivery_year,
            "image_url": self.image_url,
            "is_available": self.is_available
        }
