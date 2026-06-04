from flask import render_template, Blueprint

features_bp = Blueprint("features", __name__, template_folder="templates")

@features_bp.route("/inventory")
def inventory():
    return render_template("inventory.html")

@features_bp.route("/products")
def products():
    return render_template("products.html")

@features_bp.route("/sales")
def sales():
    return render_template("sales.html")