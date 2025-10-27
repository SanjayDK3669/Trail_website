from flask import Flask
from .config import Config
from .models import db, init_db
from .routes import api_blueprint
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv
load_dotenv()

def create_app():
    app = Flask(__name__, static_folder=None)
    app.config.from_object(Config)

    # init extensions
    db.init_app(app)
    init_db(app)

    # CORS: restrict origins in production by setting ALLOWED_ORIGINS env var
    CORS(app, resources={r"/api/*": {
        "origins": app.config.get("ALLOWED_ORIGINS", "*"),
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }})

    # Rate limiting: e.g., 10 requests per minute per IP for the submission endpoint
    limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])
    limiter.init_app(app)

    # register blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    @app.route("/", methods=["GET"])
    def root():
        return {"status": "ok", "message": "Contact API is running"}

    return app
