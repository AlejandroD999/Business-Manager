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