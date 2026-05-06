from flask import Blueprint, jsonify, request
from app import db
from app.models.price_sticker import PriceSticker

price_sticker_bp = Blueprint('price_sticker', __name__, url_prefix='/price_sticker')

# GET - NEXT AVAILABLE PRICE
@price_sticker_bp.route('/', methods=['GET'])
def get_next_available_price():
    price_sticker = PriceSticker.query.first()
    if price_sticker is None:
        return jsonify({"error": "No price sticker found"}), 404
    return jsonify(price_sticker.to_dict()), 200

# PATCH - INCREMENT NEXT AVAILABLE PRICE BY 1
@price_sticker_bp.route('/', methods=['PATCH'])
def increment_next_available_price():
    price_sticker = PriceSticker.query.first()
    if price_sticker is None:
        return jsonify({"error": "No price sticker found"}), 404
    
    price_sticker.next_avail_price = (price_sticker.next_avail_price or 0) + 1
    db.session.commit()
    
    return jsonify(price_sticker.to_dict()), 200

# POST - SET NEXT AVAILABLE PRICE POINT
@price_sticker_bp.route('/', methods=['POST'])
def set_next_available_price_point():
    data = request.get_json()
    
    new_price_sticker = PriceSticker(
        next_avail_price=data.get('next_avail_price')
    )
    
    db.session.add(new_price_sticker)
    db.session.commit()
    
    return jsonify(new_price_sticker.to_dict()), 201

