from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    userid=Column(Integer, primary_key=True)
    firstName=Column(String)
    lastName=Column(String)
