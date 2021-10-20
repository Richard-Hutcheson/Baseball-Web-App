from app_package import app
from flask import Flask, render_template, redirect, url_for, request

@app.route('/index', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['Username'] != 'admin' or request.form['Password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('/HomePage'))
    return error

@app.route('/')
@app.route('/index')
def index():
    loginStatus = login()
    return render_template("loginpage.html", error=loginStatus)

