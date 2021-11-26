from app_package import bcrypt
from app_package import app
from flask import render_template, request, flash, redirect

from app_package import db


# @app.route('/home')
# def homePage():
#     return render_template('homepage.html')
#
from app_package.Classes.user import User


@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('loginpage.html', title='Sign In')

@app.route('/dashboard')
def dashboard():
    usernameUp = "userX".upper()
    return render_template("dashboard.html", title = "Dashboard", username = usernameUp, css = "../static/dashboard.css" )

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html', title='Create Account', created='')


@app.route('/searchResults', methods=['GET', 'POST'])
def searchResults():
    return render_template('searchResults.html', title='Results')

@app.route('/handleLogin', methods=['GET', 'POST'])
def handleLogin():

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("USERNAME = ", username, "\nPASSWORD = ", password)
        user = User.query.filter_by(username=username).first()
        print("user.password = ", user.password)
        print("passwordTest = ", password)
        if user and bcrypt.check_password_hash(user.password, str(password)):
            return redirect('/dashboard')
    return redirect('/login')


@app.route('/handleRegistration', methods=['GET', 'POST'])
def handleRegistration():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # if account is valid
        user = User.query.filter_by(username=username).first()

        if not user:
            # account can be create
            # d, but first encrypt password
            encrypt_pass = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=username,password=str(encrypt_pass))
            db.session.add(user)
            db.session.commit()
            return render_template('register.html', title='Create Account', created='success')
        else:
            print("User exists")
         #if the account is invalid
        return render_template('register.html', title='Create Account', created='fail')




@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')