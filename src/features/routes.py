from flask import render_template, request, session, Blueprint, redirect, url_for
from .utils import get_year_range, string_to_date 
from .expenses_db import * 
import os

# TODO Make expense table date the same format as input

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, 
                        template_folder="templates", static_folder="static",
                        static_url_path="/src/features/static")


@features_bp.route("/expenses", methods=["GET", "POST"])
def expenses():
    username = session.get("user")
    user_id = session.get("user_id")
    
    if not username:
        redirect(url_for("auth.sign_in"))

    expenses = pull_expenses(user_id) 

    if request.method == "POST":
        start_date= request.form.get("start_date")
        end_date= request.form.get("end_date") 
        
        if not start_date or not end_date:
            # TODO Prompt error 
            print("Start and end date required")
            return
        
        expenses = pull_expenses(user_id, start_date=string_to_date(start_date), end_date=string_to_date(end_date))
        
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
