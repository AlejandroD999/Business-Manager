from flask import render_template, Blueprint
import os

CURR_DIR_PATH = os.path.dirname(__file__)

features_bp = Blueprint("features", __name__, template_folder="templates", static_folder="static",
                        static_url_path=os.path.join(CURR_DIR_PATH, "statics"))

@features_bp.route("/expenses")
def expenses():
    headers = ["id", "name", "random thing"]
    return render_template("expenses.html", table_headers=headers)

