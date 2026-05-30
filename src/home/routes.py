from flask import Blueprint, render_template, request, url_for

home_bp = Blueprint("home", __name__, 
                    template_folder="templates", static_folder="static",
                    static_url_path="/src/home/static")

@home_bp.route("/home")
def home():
    return render_template("home.html")

@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@home_bp.route("/inventory")
def inventory():
    return render_template("inventory.html")

@home_bp.route("/products")
def products():
    return render_template("products.html")

@home_bp.route("/sales")
def sales():
    return render_template("sales.html")