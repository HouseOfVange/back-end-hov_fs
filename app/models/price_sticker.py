from app import db

class PriceSticker(db.Model):
    price_sticker_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    next_avail_price = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.price_sticker_id,
            "next_avail_price": self.next_avail_price
        }
