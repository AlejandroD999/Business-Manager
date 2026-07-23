from ..extensions import db
from ..models.auth_mod import User

def add_user(username, password):
    new_user = User(username=username, password=password)

    try:
        db.session.add(new_user)

        db.session.commit()
    except Exception:
        db.session.rollback()

def user_exists(name):
    return db.session.query(User).filter_by(username=name).first() is not None

def fetch_user_id(name):
    user_data = db.session.query(User).filter_by(username=name).first()
    return user_data.id if user_data else None
    
def fetch_psw(username):
    user = db.session.query(User).filter_by(username=username).first()

    if not user.password:
        return

    if isinstance(user.password, bytes): 
        user.password.decode("utf-8") 
    return user.password 
