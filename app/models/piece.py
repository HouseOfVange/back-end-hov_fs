from app import db

# formerly Board
class Piece(db.Model):
    piece_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    client = db.Column(db.String)
    piece_description = db.Column(db.String)
    order_year = db.Column(db.Integer)
    delivery_year = db.Column(db.Integer)
    likes_count = db.Column(db.Integer)

    comment = db.relationship("Comment", backref="piece", passive_deletes=True)
