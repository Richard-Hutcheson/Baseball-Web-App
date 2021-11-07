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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/mainpage')
    return render_template('loginpage.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    return render_template("homepage.html")

@app.route('/mainpage')
def mainpage():
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #this will generate a hashed password that is 80 characters long
        hash_pass = generate_password_hash(form.password.data,method='sha256')
        #user = User(form.username.data,hash_pass)


        #db_session.add(user)
        flash('account created!')
        return redirect('/login')
    return render_template('register.html', title='Register', form=form)

