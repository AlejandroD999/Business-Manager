from .config import Config
from .extensions import db
from flask import Flask
import secrets
from datetime import timedelta

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = secrets.token_hex(32)
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(days=7)

    db.init_app(app)

    with app.app_context():
        db.reflect()

        # Db models
        from .models.auth_mod import User

    # Blueprints
    from .auth.routes import auth_bp
    from .home.routes import home_bp
    from .features.routes import features_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(features_bp)

    return app