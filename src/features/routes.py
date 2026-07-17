from flask import render_template, Blueprint

features_bp = Blueprint("features", __name__, template_folder="templates")

@features_bp.route("/inventory")
def inventory():
    return render_template("inventory.html")

@features_bp.route("/expenses")
def expenses():
    return render_template("expenses.html")

@features_bp.route("/sales")
def sales():
    return render_template("sales.html")
