from flask import render_template, session, Blueprint, redirect, url_for
from .expenses_db import * 
import os

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, template_folder="templates", static_folder="static",
                        static_url_path=os.path.join(CURR_DIR_PATH, "statics"))

@features_bp.route("/expenses")
def expenses():
    username = session.get("user")
    user_id = session.get("user_id")

    if not username:
        redirect(url_for("auth.sign_in"))

    expenses = pull_expenses(user_id)
    headers = get_headers() 
    table_headers = [] 

    if not headers:
        # TODO Handle error 
        pass
    
    for header in headers:
        if "id" not in header.lower():
            table_headers.append(header)

    return render_template("expenses.html", table_headers=table_headers, expenses=expenses)

@features_bp.route("/expenses/create-expense", methods=["GET", "POST"])
def create():
    username = session.get("user")

    if not username:
        redirect(url_for("auth.sign_in"))
    pass

@features_bp.route("/expenses/update-expense", methods=["GET", "POST"])
def update():
    pass
