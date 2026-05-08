from .extensions import db
from .config import Config
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.reflect()

        from .models.auth_mod import User
        
    return app