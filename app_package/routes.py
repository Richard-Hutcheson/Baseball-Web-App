from app_package import app
from flask.globals import session
from flask import render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from app_package import db
from app_package import engine
from sqlalchemy import text
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
    teamNames = []
    faveTeam = ''
    faveTeamYear = -1
    yearList = []
    playerList = []
    #makes sure user exists in session
    if 'username' in session:
        usernameUp = session['username']
        usernameUp = usernameUp.upper()
        #get list of teams in db
        result = engine.execute(
            text(
                '''
                SELECT teamName
                FROM teams
                GROUP BY teamName
                '''
            )
        )
        for row in result.fetchall():
            teamNames.append(row['teamName'])
        
        #GET USER'S FAVORITE TEAM AND FAVORITE TEAM YEAR
        result = engine.execute(text(
            f'''
            SELECT favoriteTeam, favoriteYear
            FROM users
            WHERE username = '{usernameUp}'
            '''
        ))

        favoritesInfo = [dict(row) for row in result.fetchall()]
        #user does have a favorite team and year
        if (favoritesInfo[0]['favoriteTeam'] != None):
            faveTeam = favoritesInfo[0]['favoriteTeam']
            ndx1 = 0
            ndx2 = 0
            for i in range(0, len(teamNames)):
                if (teamNames[i] == faveTeam):
                    ndx2 = i
            #do the swap
            temp = ndx1
            teamNames[ndx1] = teamNames[ndx2]
            teamNames[ndx2] = teamNames[temp]
            #get team's years
            result = engine.execute(text(
                f'''
                SELECT year
                FROM teams
                WHERE teamName = '{faveTeam}'
                '''
            ))
            for row in result.fetchall():
                yearList.append(row['year'])
            
            #move current fave year to front
            yearList.insert(0, 2020)
            faveTeamYear = 2020

            #GET PLAYERS FROM FAVORITE TEAM DURING SPECIFIED YEAR
            result = engine.execute(text(
                f'''
                SELECT concat(nameFirst, ' ', nameLast) as name, birthYear as birthyear, concat(birthCity, ', ', birthState, ', ', birthCountry) as birthPlace, p.personID as personID
                FROM people as p, teams as t, players as pl
                WHERE p.personID = pl.personID AND t.teamID = pl.teamID AND pl.year = '{faveTeamYear}' AND t.teamName = '{faveTeam}' AND t.year = pl.year
                GROUP BY p.personID
                ORDER BY p.nameFirst
                '''
            ))
            pitchers = engine.execute(text(
                    f'''
                    SELECT personID
                    FROM pitching as p, teams as t
                    WHERE t.teamID = p.teamID AND t.teamName = '{faveTeam}' AND t.year = '{faveTeamYear}' AND p.year = t.year AND isPostSeason = 'N'
                    '''
            ))
            pitchers = pitchers.fetchall()
            result = result.fetchall()
            for row in result:
                age = faveTeamYear - row['birthyear']
                personID = row['personID'] 
                isBatter = 'Y'
                isPitcher = 'N'
                # DETERMINE IF BATTER OR PITCHER                
                for pitcher in pitchers:
                    print(personID, " == ", pitcher['personID'])
                    if (personID == pitcher['personID']):
                        isBatter = 'N'
                        isPitcher = 'Y'
                        break
                player = {
                    'name': row['name'],
                    'age': age,
                    'birthPlace': row['birthPlace'],
                    'batter': isBatter,
                    'pitcher': isPitcher,
                }
                playerList.append(player)

        else:
            teamNames.insert(0, 'None')
            faveTeam = 'NONE'
            faveTeamYear = 'N/A'



    else:
        usernameUp = "USER_Z"
        redirect('/login')
    
    return render_template("dashboard.html", players = playerList, teamYears = yearList, 
        teamNames = teamNames, faveTeam = faveTeam, faveTeamYear = faveTeamYear, title = "Dashboard",
        username = usernameUp, css = "../static/dashboard.css")

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
            session['username'] = username
            return redirect(url_for('dashboard'))
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

@app.route('/changeFaveTeam', methods=['GET', 'POST'])
def changeFaveTeam():
    
    return redirect('/dashboard')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/login")

@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')