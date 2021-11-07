from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declartive_base()

class User(Base):
    __tablename__ = 'user'

    userid=db.Column(Integer, primary_key=True)
    firstName=db.Column(String)
    lastName=db.Column(String)
