# Baseball Web Application
CSI 3335

Team Members:
* Richard Hutcheson
* Austin Blanchard
* Noah Lambaria

## Install Instructions
1. Ensure you have correct credentials for username and password in csi3335fall2021.py
2. Follow the Create Database instructions in the section below
3. Navigate to the root project folder (Baseball-Web-App)
4. run flask with "flask run", ensure .flaskenv has FLASK_APP environment variable saved

## Running Flask Server
1. Enter Python environment and install the packages listed below
2. Within csi3335fall2021.py enter appropriate db information
3. Enter root directory
4. Type and enter "Flask run"

## Project Dependencies (using Anaconda)
* pip install python-dotenv
* conda install -c anaconda flask
* conda install -c conda-forge flask-sqlalchemy
* conda install -c conda-forge sqlalchemy-utils
* conda install -c anaconda pymysql
* conda install -c anaconda pandas
* conda install -c anaconda werkzeug

##Create database (RUN THIS BEFORE STARTING THE FLASK APP)

##MacOS 
1. Navigate to the data_cleaning directory in the project.
2. Ensure that RAN_Mac.sql, csvParser.py, and createDB_Mac.py are in data_cleaning.
3. Ensure the .csv files are in data_cleaning directory. 
4. Run the createDB_Mac.py script ("python createDB_Mac.py").
5. Congrats! database created!
##Windows
1. Navigate to the data_cleaning directory in the project.
2. Ensure that RAN_Win.sql, csvParser.py, and createDB_Win.py are present in data_cleaning.
3. Ensure the .csv files are in data_cleaning directory.
4. Run the createDB_Win.py script ("python createDB_Win.py")
5. Congrats! database should be created!