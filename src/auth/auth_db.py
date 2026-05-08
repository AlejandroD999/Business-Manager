from ..extensions import db
from ..models.auth_mod import User

def fetch_user_id(name):
    user = db.session.query(User).filter_by(username=name).first()

    return user.id if user else None

if __name__ == "__main__":
    fetch_user_id("alejandro")