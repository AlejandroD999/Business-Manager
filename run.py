from flask import Flask, Blueprint, render_template
import os

curr_dir = os.getcwd()

home = Blueprint('home', __name__, template_folder=os.path.join(curr_dir, "src/frontend/templates/home"))
auth = Blueprint('auth', __name__, template_folder=os.path.join(curr_dir, "src/frontend/templates/auth"))

app = Flask(__name__)

@home.route("/")
def home_page():
    return render_template("dashboard.html")

@auth.route("/auth")
def register():
    return render_template('register.html')


app.register_blueprint(home)
app.register_blueprint(auth)

if __name__ == "__main__":
    app.run(debug=True)


