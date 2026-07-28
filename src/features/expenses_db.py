from ..extensions import db
from ..models.expenses_mod import Expenses

def insert_expense_data(user_id, description, amount, date):
    statement = Expenses(user_id=user_id, description=description, amount=amount, date=date)
    
    try:
        db.session.add(statement)
        db.session.commit()

    except Exception:
        db.session.rollback()

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
