from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    
    # Configure rate limiter
    limiter = Limiter(
        get_remote_address,
        app=app,
        default_limits=["100 per day", "10 per minute"],
        storage_uri="memory://"
    )
    
    # Register routes
    from app.routes import translate_bp
    app.register_blueprint(translate_bp)
    
    return app, limiter