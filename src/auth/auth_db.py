from ..extensions import db
from ..models.auth_mod import User

def add_user(username, password):
    new_user = User(username=username, password=password)

    try:
        db.session.add(new_user)

        db.session.commit()
    except Exception:
        db.session.rollback()

def fetch_user_id(name):
    user_data = db.session.query(User).filter_by(username=name).first()

    return user_data.id if user_data else None
    

