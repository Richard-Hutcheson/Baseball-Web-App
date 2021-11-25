from app_package import app
from flask import render_template, redirect, request, flash, url_for
from csi3335fall2021 import user
# from Classes import User

# @app.route('/home')
# def homePage():
#     return render_template('homepage.html')
#

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
    return render_template('register.html', title='Create Account')


@app.route('/searchResults', methods=['GET', 'POST'])
def searchResults():
    return render_template('searchResults.html', title='Results')

@app.route('/handleRegistration', methods=['GET', 'POST'])
def handleLogin():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print("username = " + username + " password = " + password)
        #if account is valid
        return render_template('loginpage.html', title='Sign In')

    #if the account is invalid
    return render_template('register.html', title='Create Account')




@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')