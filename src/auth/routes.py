from .auth_db import add_user, user_exists
from flask import Blueprint, render_template
import os

auth_bp = Blueprint("auth", __name__, template_folder="templates")

@auth_bp.route("/register")
def register():
    # Manage user registration
    return render_template("register.html")
    

    if not user_exists(username):
        # Take to sign_in page
        return
    
@auth_bp.route("/sign-in")
def sign_in():
    return render_template("sign_in.html")