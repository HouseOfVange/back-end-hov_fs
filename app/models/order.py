from app import db
from datetime import datetime, timezone

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    contact = db.Column(db.String)
    the_time_to_buy_is_now = db.Column(db.Boolean)
    desire = db.Column(db.String)
    understand_that_hov_cost_money = db.Column(db.Boolean)
    status = db.Column(db.String, default='pending')
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def to_dict(self):
        return {
            "id": self.order_id,
            "name": self.name,
            "contact": self.contact,
            "the_time_to_buy_is_now": self.the_time_to_buy_is_now,
            "desire": self.desire,
            "understand_that_hov_cost_money": self.understand_that_hov_cost_money,
            "status": self.status,
            "created_at": self.created_at,
        }
    