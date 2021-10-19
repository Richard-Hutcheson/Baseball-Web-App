from app_package import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Richard'}
    return render_template("homepage.html")