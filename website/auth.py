from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/signin')
def logout():
    return render_template("signin.html")

@auth.route('/info')
def sign_up():
    return render_template("info.html")