import random
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

# Login Page
@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

#SignUp page
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
            flash('Password must be at least 7 characters', category ='error')
            pass
        else:
            # add user to database
            flash('Account created!', category='success')
    return render_template("signUp.html")

# About Page
@auth.route('/about')
def about():
    return render_template("about.html")

# Applications
@auth.route('/applications')
def applications():
    return render_template("applications.html")

# Calculator Application
@auth.route('/calculatorApp', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        # Handle calculation here
        try:
            expr = request.form['expression']
            result = eval(expr)
        except:
            result = 'E E E'
        return render_template('calculatorApp.html', result=result)
    return render_template('calculatorApp.html')

# Random Number Application [GET]
@auth.route('/randMathApp', methods=['GET'])
def get_randMathApp():
    # Declaring Variables
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])
    question = f"{num1} {operator} {num2}"
    return render_template("randMathApp.html", question=question)

# Random Number Application [POST]
@auth.route('/randMathApp', methods=['POST'])
def post_randMathApp():
    # Declaring variables
    num1 = request.form.get("num1")
    num2 = request.form.get("num2")
    operator = request.form.get("operator")
    user_answer = request.form.get("user_answer")
    correct_answer = 0
    result = "Your answer is..."
    try: # Create Calculatons based on operator
        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        elif operator == '*':
            correct_answer = num1 * num2
        elif operator == '/':
            correct_answer = num1 / num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    try:
        if float(user_answer) == float(correct_answer):
            result = "Correct!"
        else:
            result = "Incorrect. Try again."
    except ValueError: # user_answer did not contain an integer
        result = "Invalid number!"
    return render_template("randMathResult.html", correct_answer=correct_answer, result=result, user_answer=user_answer)

# Memory Bank
@auth.route('/memBankApp', methods=['GET', 'POST'])
def randMathApp():
    return render_template("memBankApp.html")