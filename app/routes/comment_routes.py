from flask import Blueprint, jsonify, request
from app import db
from app.models.comment import Comment
from app.models.piece import Piece

comment_bp = Blueprint('comment', __name__, url_prefix='/pieces')


# CREATE NEW COMMENT
@comment_bp.route('/<int:piece_id>/comments', methods=['POST'])
def create_comment(piece_id):
    piece = Piece.query.get(piece_id)
    if piece is None:
        return jsonify({"error": f"Piece {piece_id} not found"}), 404
    
    data = request.get_json()
    
    new_comment = Comment(
        author=data.get('author'),
        message=data.get('message'),
        piece_id=piece_id
    )
    
    db.session.add(new_comment)
    db.session.commit()
    
    return jsonify(new_comment.to_dict()), 201

# DELETE - ONE COMMENT
@comment_bp.route('/<int:piece_id>/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(piece_id, comment_id):

    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401 

    comment = Comment.query.get(comment_id)
    if comment is None:
        return jsonify({"error": f"Comment {comment_id} not found"}), 404
    
    db.session.delete(comment)
    db.session.commit()
    
    return jsonify({"message": f"Comment {comment_id} successfully deleted"}), 200

# DELETE - ALL COMMENTS
@comment_bp.route('/comments', methods=['DELETE'])
def delete_all_comments():

    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401 
    
    deleted = Comment.query.delete()
    db.session.commit()
    return jsonify({"message": f"{deleted} comments deleted"}), 200
