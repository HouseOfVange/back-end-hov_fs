from flask import Blueprint, jsonify, request
from app import db
from app.models.order import Order
import os

order_bp = Blueprint('order', __name__, url_prefix='/order')

# POST - CREATE NEW ORDER
@order_bp.route('/', methods=['POST'])
def create_order():
    
    data = request.get_json()
    
    new_order = Order(
        name=data.get('name'),
        contact=data.get('contact'),
        the_time_to_buy_is_now=data.get('the_time_to_buy_is_now'),
        desire=data.get('desire'),
        understand_that_hov_cost_money=data.get('understand_that_hov_cost_money'),
    )
    
    db.session.add(new_order)
    db.session.commit()
    
    return jsonify(new_order.to_dict()), 201

# GET - GET ALL ORDERS
@order_bp.route('/', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.to_dict() for order in orders]), 200

# GET - GET ORDERS BY STATUS
@order_bp.route('/status/<string:status>', methods=['GET'])
def get_orders_by_status(status):
    orders = Order.query.filter_by(status=status).all()
    return jsonify([order.to_dict() for order in orders]), 200

# GET - GET ORDER BY ID
@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": f"Order {order_id} not found"}), 404
    return jsonify(order.to_dict()), 200

# PATCH - UPDATE ORDER STATUS BY ID
@order_bp.route('/<int:order_id>', methods=['PATCH'])
def update_order_status(order_id):
    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": f"Order {order_id} not found"}), 404
    
    data = request.get_json() or {}
    order.status = data.get('status', order.status)
    db.session.commit()
    
    return jsonify(order.to_dict()), 200

# DELETE - DELETE ORDER BY ID
@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401

    order = Order.query.get(order_id)
    if order is None:
        return jsonify({"error": f"Order {order_id} not found"}), 404
    
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": f"Order {order_id} successfully deleted"}), 200

# DELETE - DELETE ALL ORDERS
@order_bp.route('/', methods=['DELETE'])
def delete_all_orders():
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401
    
    deleted = Order.query.delete()
    db.session.commit()
    return jsonify({"message": f"{deleted} orders deleted"}), 200
