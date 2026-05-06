from flask import Blueprint, jsonify, request
from app.models.piece import Piece
from app import db

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
        image_url=data.get('image_url'),
        is_available=data.get('is_available')
    )
    
    db.session.add(new_piece)
    db.session.commit()
    
    return jsonify(new_piece.to_dict()), 201

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
