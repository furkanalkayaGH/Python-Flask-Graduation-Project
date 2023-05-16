from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/about')
def logout():
    return render_template("about.html")

@auth.route('/info')
def sign_up():
    return render_template("info.html")