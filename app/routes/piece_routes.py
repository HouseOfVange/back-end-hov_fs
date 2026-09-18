from flask import Blueprint, jsonify, request
from app.models.piece import Piece
from app import db
import os

piece_bp = Blueprint('piece', __name__, url_prefix='/pieces')

# GET - ALL PIECES
@piece_bp.route('/', methods=['GET'])
def get_all_pieces():
    all_pieces = Piece.query.all()
    return jsonify([piece.to_dict() for piece in all_pieces]), 200

# GET - ONE PIECE BY SUPPLYING piece_id
@piece_bp.route('/<int:piece_id>', methods=["GET"])
def get_one_piece(piece_id):
    piece = Piece.query.get(piece_id)
    if piece is None:
        return jsonify({"error": f"Piece {piece_id} not found"}), 404
    return jsonify(piece.to_dict()), 200

# GET - ALL COMMENTS BY SUPPLYING piece_id
@piece_bp.route('/<int:piece_id>/comments', methods=['GET'])
def get_comments_for_piece(piece_id):
    piece = Piece.query.get(piece_id)
    if piece is None:
        return jsonify({"error": f"Piece {piece_id} not found"}), 404
    return jsonify([comment.to_dict() for comment in piece.comment]), 200

# POST - NEW PIECE
@piece_bp.route('/', methods=['POST'])
def create_piece():
    data = request.get_json()
    
    new_piece = Piece(
        title=data.get('title'),
        client=data.get('client'),
        piece_description=data.get('description'),
        order_year=data.get('order_year'),
        delivery_year=data.get('delivery_year'),
        images=data.get('images'),
        is_available=data.get('is_available')
    )
    
    db.session.add(new_piece)
    db.session.commit()
    
    return jsonify(new_piece.to_dict()), 201

# PATCH - UPDATE ANY PIECE FIELD
@piece_bp.route('/<int:piece_id>', methods=['PATCH'])
def update_piece(piece_id):
    piece = Piece.query.get(piece_id)
    if piece is None:
        return jsonify({"error": f"Piece {piece_id} not found"}), 404
    
    data = request.get_json()

    if 'title' in data:
        piece.title = data['title']

    if 'client' in data:
        piece.client = data['client']

    if 'description' in data:
        piece.piece_description = data['description']

    if 'order_year' in data:
        piece.order_year = data['order_year']

    if 'delivery_year' in data:
        piece.delivery_year = data['delivery_year']

    if 'is_available' in data:
        piece.is_available = data['is_available']

    if 'new_image' in data:
        current_images = piece.images or []
        current_images.append(data['new_image'])
        piece.images = current_images

    if 'images' in data:
        piece.images = data['images']

    db.session.commit()
    return jsonify(piece.to_dict()), 200

# DELETE - ONE PIECE
@piece_bp.route('/<int:piece_id>', methods=['DELETE'])
def delete_piece(piece_id):
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401 

    piece = Piece.query.get(piece_id)
    if piece is None:
        return jsonify({"error": f"Piece {piece_id} not found"}), 404
    
    db.session.delete(piece)
    db.session.commit()
    
    return jsonify({"message": f"Piece {piece_id} successfully deleted"}), 200

# DELETE - ALL PIECES
@piece_bp.route('/', methods=['DELETE'])
def delete_all_pieces():
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401 

    deleted = Piece.query.delete()
    db.session.commit()
    return jsonify({"message": f"{deleted} pieces deleted"}), 200
