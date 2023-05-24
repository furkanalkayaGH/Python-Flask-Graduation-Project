from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if email == '':
            flash('Please fill the e-mail section', category='error')
        elif firstName == '':
            flash('Please fill the name section', category='error')
        elif password1 == '':
            flash('Please fill the password section', category='error')
        elif password2 == '':
            flash('Please fill the password confirm section', category='error')

                
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash("Passwords don't match.", category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')        
    data = request.form
    print(data)
    return render_template("signup.html")

@auth.route('/sign-in', methods=['GET','POST'])
def login():
    return render_template("signin.html")

@auth.route('/info')
def info():
    return render_template("info.html")