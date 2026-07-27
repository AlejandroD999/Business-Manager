from flask import render_template, session, Blueprint, redirect, url_for
from .expenses_db import get_headers, pull_expenses
import os

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, template_folder="templates", static_folder="static",
                        static_url_path=os.path.join(CURR_DIR_PATH, "statics"))

@features_bp.route("/expenses")
def expenses():
    username = session.get("User")
    
    if not username:
        redirect(url_for("auth.sign_in"))
    
    expenses = pull_expenses()
    headers = get_headers() 
    
    headers.remove("id")
    headers.remove("user_id")
        
    return render_template("expenses.html", table_headers=headers, expenses=expenses)

@features_bp.route("/expenses/update-expense", methods=["GET", "POST"])
def update_expense():
    pass
