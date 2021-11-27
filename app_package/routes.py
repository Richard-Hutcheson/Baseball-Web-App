from werkzeug.utils import redirect
from app_package import app
from flask import render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from app_package import db
from app_package.Classes.user import User

'''
Future Richard, consider using sessions to pass data through redirection 
without exposing information in the url heading. If you are okay with
showing details in the url, then consider a dictionary being passed
through url_for and then iterate over them with jinja by parsing over
them with request.args.get('')

-Past Richard

'''



@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('loginpage.html', title='Sign In')

@app.route('/dashboard')
def dashboard():

    usernameUp = request.args.get('username')
    if usernameUp is not None:
        usernameUp = usernameUp.upper()
    else:
        usernameUp = "USER_Z"

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

        user = User.query.filter_by(username=username).first()
        #user is valid, log them in
        if user and check_password_hash(user.password,password):
            return redirect(url_for('dashboard', username = username))
            #return render_template("dashboard.html", title = "Dashboard", username = username, css = "../static/dashboard.css" )

    return redirect("/login")


@app.route('/handleRegistration', methods=['GET', 'POST'])
def handleRegistration():
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # if account is valid
        user = User.query.filter_by(username=username).first()

        if not user:
            # account can be created, but first encrypt password
            encrypt_pass = generate_password_hash(password)
            user = User(username=username,password=encrypt_pass)
            db.session.add(user)
            db.session.commit()
            return render_template('register.html', title='Create Account', created='success')
        else:
            print("User exists")
         # if the account is invalid
        return render_template('register.html', title='Create Account', created='fail')




@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')