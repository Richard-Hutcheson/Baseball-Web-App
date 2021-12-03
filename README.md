# Baseball Web Application
CSI 3335

Team Members:
* Richard Hutcheson
* Austin Blanchard
* Noah Lambaria


## Install Instructions
* 

# Project Dependencies (using Anaconda
* pip install python-dotenv
* conda install -c anaconda flask
* conda install -c conda-forge flask-sqlalchemy
* conda install -c conda-forge sqlalchemy-utils
* conda install -c anaconda pymysql
* conda install -c anaconda pandas
* conda install -c anaconda werkzeug

#Create database (RUN THIS BEFORE STARTING THE FLASK APP)

#MacOS 
* Navigate to the data_cleaning directory in the project.
* Ensure that RAN_Mac.sql, csvParser.py, and createDB_Mac.py are in data_cleaning.
* Ensure the .csv files are in data_cleaning directory. 
* Run the createDB_Mac.py script ("python createDB_Mac.py").
* Congrats! database should be created!

#Windows
* Navigate to the data_cleaning directory in the project.
* Ensure that RAN_Win.sql, csvParser.py, and createDB_Win.py are present in data_cleaning.
* Ensure the .csv files are in data_cleaning directory.
* Run the createDB_Win.py script ("python createDB_Win.py")
* Congrats! database should be created!