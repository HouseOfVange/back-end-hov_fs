from app import db

class Price_Sticker(db.Model):
    price_sticker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    next_avail_price = db.Column(db.Integer)
