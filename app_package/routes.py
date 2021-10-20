from app_package import app
from flask import Flask, render_template, redirect, url_for, request, flash
from forms import LoginForm

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
        return redirect('/home')
    return render_template('loginpage.html', title='Sign In', form=form)

@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    return render_template("loginpage.html")

