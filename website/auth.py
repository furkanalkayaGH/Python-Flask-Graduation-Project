from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from PIL import Image
import os
from werkzeug.utils import secure_filename
from website.ocr import extract_text


auth = Blueprint('auth', __name__)


@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist', category='error')
        elif email == '':
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
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    data = request.form
    print(data)
    return render_template("signup.html", user=current_user)


@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        elif email == '':
            flash('Please fill the Email section.', category='error')
        elif password == '':
            flash('Please fill the Password section.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("signin.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))


@auth.route('/ocr', methods=['GET', 'POST'])
@login_required
def ocr():
    if request.method == 'POST':
        image_file = request.files.get('image_file')
        content_title = image_file.filename
        upload_dir = os.path.join(os.getcwd(), "website", "uploads")
        image_file.save(os.path.join(upload_dir, content_title))
        img = Image.open(os.path.join(upload_dir, content_title))
        if image_file not in request.files:
            #flash("Please select a file", category='error')
            return render_template("ocr.html", user=current_user)
        return {"msg": extract_text(img)}
    return render_template("ocr.html", user=current_user)

# def allowed_file(filename):
    # return '.' in filename and \
    # filename.rsplit('.',1).lower() in ALLOWED_EXTENSIONS
