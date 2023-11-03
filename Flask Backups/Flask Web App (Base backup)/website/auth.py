from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", userText="Testing")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password = request.form.get('password')
        passwordCon = request.form.get('passwordCon')

        # String input validations
        if len(email) < 4:
            flash('Email must be greater than 3 characters!', category ='error')
            pass
        elif len(firstName) < 2:
            flash('Email must be greater than 1 characters!', category ='error')
            pass
        elif password != passwordCon:
            flash('Passwords don\'t match!', category ='error')
            pass
        elif len(password) < 7:
            flash('EPassword must be at least 7 characters', category ='error')
            pass
        else:
            # add user to database
            flash('Account created!', category='success')
    return render_template("signUp.html")

