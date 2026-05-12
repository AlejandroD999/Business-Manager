from src.factory import create_app
from src.extensions import db
from src.auth import auth_db



app = create_app()

@app.route("/auth")
def index():
    auth_db.register_user("Ale", "4321")
    return f"{auth_db.fetch_user_id("Ale")}"

if __name__ == "__main__":
    app.run(debug=True)