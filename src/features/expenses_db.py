from ..extensions import db
from ..models.expenses_mod import Expenses

def insert_expense(user_id, description, amount, date):
    statement = Expenses(user_id=user_id, description=description, amount=amount, date=date)
    
    try:
        db.session.add(statement)
        db.session.commit()

    except Exception:
        print("Error creating expense")
        db.session.rollback()

def update_expense(expense_id, new_description=None, new_amount=None, new_date=None):
    
    expense = pull_expense(expense_id)
    
    if new_description:
        expense.description = new_description

    if new_amount:
        expense.amount = new_amount

    if new_date:
        expense.date = new_date
    
    try:
        db.session.commit()

    except Exception:
        print("Error updating expense")
        db.session.rollback()

def get_headers():
    return [column.name.capitalize() for column in Expenses.__table__.columns]

def pull_expense(expense_id):
    if not expense_id:
        # TODO Handle Error
        return

    expense = db.session.execute(db.select(Expenses).filter_by(id=expense_id)).scalar_one()

    return expense
    

def pull_expenses(user_id, date_obj=None):
    # Fetch and return expenses in rows [Expenses>1, Expenses>2, ...]
    
    if date_obj:
        start_date = date(date_obj.year, date_obj.month, 1)

        if start_date.month == 12:
            end_date = date(date_obj.year + 1, 1, 1)
        else:
            end_date = date(date_obj.year, date_obj.month + 1, 1)

        expense = db.session.scalars(db.select(Expenses).where(
            Expenses.user_id==user_id,
            Expenses.date >= start_date,
            Expenses.date < end_date)).all()

        return expense
    
    return db.session.scalars(db.select(Expenses).filter_by(user_id=user_id)).all()

def delete_expense(expense_id):
    expense = pull_expense(expense_id)


    try:
        db.session.delete(expense)
        db.session.commit()

    except Exception:
        print("Error deleting expense")
        db.session.rollback()

