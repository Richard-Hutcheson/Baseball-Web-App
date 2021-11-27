# Baseball Web Application
CSI 3335

Team Members:
* Richard Hutcheson
* Austin Blanchard
* Noah Lambaria


## Install Instructions
* 
## Imported Modules
* OS
* Flask
* CSV


# Anaconda Dependencies
* conda install -c conda-forge flask-sqlalchemy
* conda install -c conda-forge sqlalchemy-utils
* conda install -c anaconda colorama
* conda install -c anaconda pymysql
* pip install python-dotenv
* conda install -c anaconda flask
* conda install -c anaconda flask-wtf (not currently needed)
* conda install -c conda-forge flask-bcrypt
* werkzeug

TIP:

you can export your Anaconda environment using:\
"conda env export > <environment_file>.yml" 
*make sure to activate the environment you want to export first*


and recreate it using:\
"conda env create -f <environment_file>.yml"

run flask with "flask run", ensure .flaskenv has FLASK_APP environment variable saved

#SQL BaseballAPP.sql instructions
* run csvParser.py
* copy all CSVs /usr/local/var/mysql/baseballAPP/
* go to current directory of the BaseballApp.sql script and run in SQL
