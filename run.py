from src.factory import create_app
from src.extensions import db

app = create_app()

from src.models.auth_mod import Users

@app.route("/auth")
def index():
    user = db.session.execute(db.select(Users)).scalars().all()
    
    return "<pre>" + "\n".join(
        f"{u.username}|{u.password}"
        for u in user) + "</pre>"
 
@app.route("/test-db")
def test():
    try:
        db.session.execute(db.text("SELECT 1"))
        return "DB Connected"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    app.run(debug=True)