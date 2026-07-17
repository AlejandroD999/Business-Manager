from flask import render_template, Blueprint

features_bp = Blueprint("features", __name__, template_folder="templates")

@features_bp.route("/expenses")
def expenses():
    return render_template("expenses.html")

