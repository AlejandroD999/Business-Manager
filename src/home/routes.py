from flask import Blueprint, render_template, session, url_for, redirect

home_bp = Blueprint("home", __name__, 
                    template_folder="templates", static_folder="static",
                    static_url_path="/src/home/static")

@home_bp.route("/")
def home():
    username = session.get("user")

    if not username:
        return redirect(url_for("auth.sign_in"))
    
    return render_template("home.html")

@home_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@home_bp.route("/products")
def products():
    username = session.get("user")

    if not username:
        return redirect(url_for("auth.sign_in"))
    
    return render_template("products.html")