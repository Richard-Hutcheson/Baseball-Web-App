from app_package import app
]from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Numeric, create_engine
from csi3335fall2021 import user
import pymysql

Base = declarative_base()


class User(db.Model):
    __tablename__ = "users"
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(50))
    favoriteTeam = db.Column(db.String(255))
    favoriteYear = db.Column(db.Integer)

