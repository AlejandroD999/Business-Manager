from flask import render_template, request, session, Blueprint, redirect, url_for
from .utils import get_year_range, string_to_date 
from .expenses_db import * 
import os

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, template_folder="templates", static_folder="static", static_url_path="/src/features/static")


@features_bp.route("/expenses", methods=["GET", "POST"])
def expenses():
    username = session.get("user")
    user_id = session.get("user_id")
    
    if not username:
        redirect(url_for("auth.sign_in"))

    expenses = pull_expenses(user_id) 
    print("B4", expenses)

    if request.method == "POST":
        filter_month = request.form.get("month")
        filter_year = request.form.get("year") 
        filter_date = string_to_date(f"{filter_month}/{filter_year}", date_format="%m/%Y") 
        print(59)
        expenses = pull_expenses(user_id, filter_date)
    print("After", expenses)
    headers = get_headers() 
    years = get_year_range()
    table_headers = [] 

    if not headers:
        # TODO Handle error 
        pass
    
    for header in headers:
        if "id" not in header.lower():
            table_headers.append(header)

    return render_template("expenses.html",
                           table_headers=table_headers,
                           expenses=expenses,
                           years=years)

@features_bp.route("/filter-expenses", methods=["POST"])
def filter_expenses():
    month = request.form.get("month")
    year = request.form.get("year")

    return redirect(url_for("features.expenses"))

@features_bp.route("/expenses/create-expense", methods=["GET", "POST"])
def create():
    username = session.get("user")

    if not username:
        redirect(url_for("auth.sign_in"))
    pass

@features_bp.route("/expenses/update-expense", methods=["GET", "POST"])
def update():
    pass
