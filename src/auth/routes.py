from .auth_db import add_user, user_exists, fetch_psw
from .utils import valid_username
from flask import Blueprint, request, render_template, redirect, url_for
import bcrypt

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    # Manage user registration
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")


        if valid_username(username) and not user_exists(username):
            # TODO Make username + password criteria
            # TODO Encrypt Password
            
            bcrypt.hashpw(password.encode(), bcrypt.gensalt())

            add_user(username, password)


            return redirect(url_for("auth.sign_in"))

    return render_template("register.html")
    
@auth_bp.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        usr = request.form.get("username")
        psw = request.form.get("password")

        if user_exists(usr) and bcrypt.checkpw(psw.encode(), fetch_psw(usr)):
            return "Succcess"
        
    return render_template("sign_in.html")
