from flask.globals import session
from flask import render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from app_package import db, engine, app
from sqlalchemy import text, update
from app_package.Classes.user import User

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
        #user DOES have a favorite team and year
        if ('tempFaveTeam' in session or favoritesInfo[0]['favoriteTeam'] != None):
            if ('tempFaveTeam' in session):
                tempFaveTeam = session['tempFaveTeam']
                print("FAVE TEAM = ", tempFaveTeam)
                session.pop('tempFaveTeam', None)
            else:
                tempFaveTeam = faveTeamYear
                tempFaveTeam = faveTeam

            faveTeam = favoritesInfo[0]['favoriteTeam']
            ndx1 = 0
            ndx2 = 0
            
            for i in range(0, len(teamNames)):
                if (teamNames[i] == tempFaveTeam):
                    ndx2 = i
            #do the swap
            temp = teamNames[ndx1]
            teamNames[ndx1] = teamNames[ndx2]
            teamNames[ndx2] = temp

            #get team's years
            result = engine.execute(text(
                f'''
                SELECT year
                FROM teams
                WHERE teamName = '{tempFaveTeam}'
                '''
            ))
            for row in result.fetchall():
                yearList.append(row['year'])
            
            #retrieve fave year if it exists and move current fave year to front if it exists
            faveTeamYear = 2020
            if 'faveYear' in session:
                faveTeamYear = session['faveYear']
                session.pop('faveYear', None)
            yearList.insert(0, faveTeamYear)


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
                if (isinstance(row['birthyear'], int) ):
                    age = int(faveTeamYear) - int(row['birthyear'])
                else:
                    age = 'unknown'
                personID = row['personID'] 
                isBatter = 'Y'
                isPitcher = 'N'
                # DETERMINE IF BATTER OR PITCHER                
                for pitcher in pitchers:
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

    year = request.form.get('year')
    print(str(year))

    if 'username' in session:
        usernameUp = session['username']
        usernameUp = usernameUp.upper()
        #get list of teams in db
        result = engine.execute(
            text(
                f'''
                SELECT t.teamName, l.leagueName, t.divisionID, t.Wins, t.Losses
                FROM teams t JOIN Leagues l ON(t.leagueID = l.leagueID)
                WHERE t.year = '{year}'
                ORDER BY t.leagueID, t.divisionID
                '''
            )
        )
        # Query to grab only the winners (who will have a GB of 0)
        GBWinners = engine.execute(
            text(
                f'''
                SELECT t1.teamName, l1.leagueName, t1.divisionID,(t1.Wins/t1.GamesPlayed) as 'PCT',t1.Wins
                FROM Teams t1 JOIN Leagues l1 ON(t1.leagueID = l1.leagueID)
                WHERE t1.year = '{year}' AND (t1.Wins/t1.GamesPlayed) IN (
                    SELECT MAX(t.Wins/t.GamesPlayed)
                    FROM Teams t JOIN Leagues l ON(t.leagueID = l.leagueID)
                    WHERE t.year = '{year}' AND t1.leagueID = t.leagueID and t1.divisionID = t.divisionID 
                    GROUP BY t.leagueID, t.divisionID
                )
                GROUP BY t1.leagueID, t1.divisionID;
                '''
            )
        )
        # Query to fetch all the teams (including the winners)
        GBOthers = engine.execute(
            text(
                f'''
                SELECT t1.teamName, l1.leagueName, t1.divisionID,(t1.Wins/t1.GamesPlayed) as 'PCT', t1.Wins
                FROM Teams t1 JOIN Leagues l1 ON(t1.leagueID = l1.leagueID)
                WHERE t1.year = '{year}' 
                GROUP BY t1.leagueID, t1.divisionID, t1.teamName;
                '''
            )
        )


        checker = 0
        map = dict()
        for rowONE in GBOthers.fetchall():
            # reset boolean
            checker = 0
            for rowTWO in GBWinners.fetchall:
                if rowONE['teamName'] == rowTWO['teamName']:
                    # their GB will be 0
                    map[rowONE['teamName']] = 0
                    checker = 1

            # If it still wasn't found then do calculations
            if checker == 0:
                for rowTWO in GBWinners.fetchall:
                    if rowONE['leagueName'] == rowTWO['leagueName'] and rowONE['divisionID'] == rowTWO['divisionID']:
                        map[rowONE['teamName']] = ((rowTWO['Wins'] - rowONE['Wins'] ))




        for row in GBWinners.fetchall():
            print(row['teamName'] + " " + str(row['PCT']))


        return render_template('searchResults.html', title='Results',output_data=result.fetchall())

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
    
    if request.method == 'POST':
        faveTeam = request.form.get('teamSelect')
        faveTeamYear = request.form.get("faveYearSelect")
        engine.execute( text(
            f'''
            UPDATE users
            SET favoriteTeam = '{faveTeam}'
            WHERE username = '{session['username']}'
            '''    
        ))
        session['faveYear'] = faveTeamYear
        redirect('/dasboard')
    return redirect('/dashboard')

@app.route('/handleYearChange', methods=['GET', 'POST'])
def handleYearChange():
    faveTeam = request.args.get('team')
    if (faveTeam != None):
        session['tempFaveTeam'] = faveTeam

    return redirect("/dashboard")



@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if 'username' in session:
        session.pop('username', None)
    return redirect("/login")

@app.errorhandler(404)
def not_found(e):
    return render_template('pageNotFound.html')