from .auth_db import add_user, user_exists, fetch_psw
from .utils import valid_username
from flask import Blueprint, request, session, render_template, redirect, url_for
import bcrypt

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Manage user registration
    if request.method == "POST":
        username = request.form.get("username")
        psw = request.form.get("password")

        if not username or not psw:
            # TODO Make alert for invalid input
            return render_template("register.html")

        if valid_username(username) and not user_exists(username):
            # TODO Make username + password criteria
            # TODO Encrypt Password
            
            hashed_psw = bcrypt.hashpw(psw.encode(), bcrypt.gensalt())

            add_user(username, hashed_psw)

            return redirect(url_for("auth.sign_in"))

    return render_template("register.html")
    
@auth_bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        usr = request.form.get("username")
        psw = request.form.get("password")

        if not user_exists(usr) or not psw:
            # TODO Make invalid input alert
            return render_template("sign_in.html")
        
        # TODO Exception handling (salt error etc...)
        valid_psw = bcrypt.checkpw(psw.encode(), fetch_psw(usr).encode())

        if valid_psw:
            session.permanent = True
            session["user"] = usr
            return redirect(url_for("home.home"))


    return render_template("sign_in.html")