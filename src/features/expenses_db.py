from ..extensions import db
from ..models.expenses_mod import Expenses

def create_expense():
    pass

def update_expense():
    pass

def get_headers():
    return [column.name.capitalize() for column in Expenses.__table__.columns]

def pull_expenses():
    # Fetch and return expenses in rows [Expenses>1, Expenses>2, ...]
    # TODO Be user specific
    return db.session.scalars(db.select(Expenses)).all()

def delete_expense():
    pass
