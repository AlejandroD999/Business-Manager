from .extensions import db
from .config import Config
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

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