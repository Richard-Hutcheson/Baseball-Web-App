from flask_bcrypt import Bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from myConfig import Config
from csi3335fall2021 import user
import pymysql

app = Flask(__name__)

# create a new database in terminal called baseballapp
engineUrl = 'mysql+pymysql://' + user['username'] + ':' + user['password'] + '@' + user['host'] + ':3306/' + user['db']
app.config['SQLALCHEMY_DATABASE_URI'] = engineUrl
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)

engine = create_engine(engineUrl)

if not database_exists(engine.url):
    create_database(engine.url)

db = SQLAlchemy(app)

# KEEP THIS
from app_package import routes

# Create all the tables
db.create_all()