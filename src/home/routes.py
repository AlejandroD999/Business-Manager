from flask import Blueprint, render_template, request

home_bp = Blueprint("home", __name__, template_folder="templates")

@home_bp.route("/home")
def home():
    return render_template("dashboard.html")
