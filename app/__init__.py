from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "SQLALCHEMY_DATABASE_URI")

    # Import models for Alembic setup    
    from app.models.price_sticker import PriceSticker
    from app.models.piece import Piece
    from app.models.comment import Comment
    from app.models.guestbook_entry import GuestbookEntry
    from app.models.order import Order

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints 
    from .routes.price_sticker_routes import price_sticker_bp
    app.register_blueprint(price_sticker_bp)

    from .routes.piece_routes import piece_bp
    app.register_blueprint(piece_bp)

    from .routes.comment_routes import comment_bp
    app.register_blueprint(comment_bp)

    from .routes.guestbook_routes import guestbook_bp
    app.register_blueprint(guestbook_bp)

    from .routes.order_routes import order_bp
    app.register_blueprint(order_bp)

    CORS(app)
    return app
