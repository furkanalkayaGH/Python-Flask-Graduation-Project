from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if email == '':
            flash('Please fill the e-mail section', category='error')
        elif first_name == '':
            flash('Please fill the name section', category='error')
        elif password1 == '':
            flash('Please fill the password section', category='error')
        elif password2 == '':
            flash('Please fill the password confirm section', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))  
              
    data = request.form
    print(data)
    return render_template("signup.html")

@auth.route('/sign-in', methods=['GET','POST'])
def login():
    return render_template("signin.html")

@auth.route('/info')
def info():
    return render_template("info.html")