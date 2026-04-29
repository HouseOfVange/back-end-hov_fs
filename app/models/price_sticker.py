from app import db

# formerly Board
class Price_Sticker(db.Model):
    price_sticker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    next_avail_price = db.Column(db.Integer)

    comment = db.relationship("Comment", backref="piece", passive_deletes=True)
