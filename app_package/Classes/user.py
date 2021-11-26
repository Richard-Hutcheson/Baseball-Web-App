from app_package import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from csi3335fall2021 import user
import pymysql
from app_package import db


class User(db.Model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    # Although its set at 50 max for the pass, the hashed will exceed
    password = db.Column(db.String(255))
    favoriteTeam = db.Column(db.String(255))
    favoriteYear = db.Column(db.Integer)

    def __init__(self, username,password, favoriteTeam=None, favoriteYear=None):
        self.username = username
        self.password = password
        self.favoriteTeam = favoriteTeam
        self.favoriteYear = favoriteYear
