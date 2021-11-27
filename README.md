# Baseball Web Application
CSI 3335

Team Members:
* Richard Hutcheson
* Austin Blanchard
* Noah Lambaria


## Install Instructions
* 

# Anaconda Dependencies
* conda install -c conda-forge flask-sqlalchemy
* conda install -c conda-forge sqlalchemy-utils
* conda install -c anaconda colorama
* conda install -c anaconda pymysql
* pip install python-dotenv
* conda install -c anaconda flask
* conda install -c anaconda pandas
* werkzeug

TIP:

conda list --export > package-list.txt
conda create -n myenv --file package-list.txt

run flask with "flask run", ensure .flaskenv has FLASK_APP environment variable saved

#SQL BaseballAPP.sql instructions
* run csvParser.py
* copy all CSVs /usr/local/var/mysql/baseballAPP/
* go to current directory of the BaseballApp.sql script and run in SQL

#SQL BaseballApp.sql instructions for Windows
* copy csi3335fall2021.py into same dir as csvParser.py
* copy paste all cleaned csv files into MYSQL/bin/baseballapp/
* move baseballAPP.sql to MYSQL/ and run from SQL terminal