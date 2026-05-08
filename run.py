from src.factory import create_app
from src.extensions import db
from src.auth import auth_db



app = create_app()

@app.route("/auth")
def index():
    return f"{auth_db.fetch_user_id("alejandro")}"

if __name__ == "__main__":
    app.run(debug=True)