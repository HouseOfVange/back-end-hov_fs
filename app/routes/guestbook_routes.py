from flask import Blueprint, jsonify, request
from app import db
from app.models.guestbook_entry import GuestbookEntry
import os
from datetime import datetime, timezone

guestbook_bp = Blueprint('guestbook_entry', __name__, url_prefix='/guestbook')

# GET - ALL GUESTBOOK ENTRIES
@guestbook_bp.route('/', methods=['GET'])
def get_guestbook_entries():
    entries = GuestbookEntry.query.all()
    return jsonify([entry.to_dict() for entry in entries]), 200

# POST - NEW GUESTBOOK ENTRY
@guestbook_bp.route('/', methods=['POST'])
def create_guestbook_entry():
    
    data = request.get_json()
    
    new_guestbook_entry = GuestbookEntry(
        author=data.get('author'),
        message=data.get('message'),
        created_at=datetime.now(timezone.utc)
    )
    
    db.session.add(new_guestbook_entry)
    db.session.commit()
    
    return jsonify(new_guestbook_entry.to_dict()), 201

# PATCH - INCREMENT GUESTBOOK ENTRY LIKES BY 1
@guestbook_bp.route('/<int:entry_id>/likes', methods=['PATCH'])
def increment_likes(entry_id):
    entry = GuestbookEntry.query.get(entry_id)
    if entry is None:
        return jsonify({"error": f"Guestbook entry {entry_id} not found"}), 404
    
    entry.likes_count = (entry.likes_count or 0) + 1
    db.session.commit()
    
    return jsonify(entry.to_dict()), 200

# DELETE - ONE GUESTBOOK ENTRY
@guestbook_bp.route('/<int:entry_id>', methods=['DELETE'])
def delete_guestbook_entry(entry_id):
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401 

    entry = GuestbookEntry.query.get(entry_id)
    if entry is None:
        return jsonify({"error": f"Guestbook entry {entry_id} not found"}), 404
    
    db.session.delete(entry)
    db.session.commit()
    
    return jsonify({"message": f"Guestbook entry {entry_id} successfully deleted"}), 200

# DELETE - ALL GUESTBOOK ENTRIES
@guestbook_bp.route('/', methods=['DELETE'])
def delete_all_guestbook_entries():
    data = request.get_json() or {}
    if data.get('password') != os.environ.get('ADMIN_PASSWORD'):
        return jsonify({"error": "Unauthorized"}), 401  

    deleted = GuestbookEntry.query.delete()
    db.session.commit()
    return jsonify({"message": f"{deleted} entries deleted"}), 200