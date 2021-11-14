from app_package import app
from flask import render_template, redirect, request, flash
from LoginForm import LoginForm
from RegisterForm import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
#from User import User

# @app.route('/home')
# def homePage():
#     return render_template('homepage.html')
#

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/mainpage')
    return render_template('loginpage.html', title='Sign In', form=form)


@app.route('/mainpage')
def mainpage():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    return render_template('register.html', title='Create Account')

@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')