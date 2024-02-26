"""ROTAS DA HOME"""

from flask import Blueprint, render_template


home_app = Blueprint("home_app", __name__)

    
@home_app.route("/")
def home():
    return render_template("pages/index.jinja")