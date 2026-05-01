from sqlalchemy import inspect
from src.factory import db, create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)