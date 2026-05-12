from src.factory import create_app
from src.extensions import db
from src.auth import auth_db



app = create_app()

@app.route("/auth")
def index():
    return f"{auth_db.user_exists("A")}"

if __name__ == "__main__":
    app.run(debug=True)