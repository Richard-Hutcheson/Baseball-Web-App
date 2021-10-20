from flask import Flask
from myConfig import Config

app = Flask(__name__)
app.config.from_object(Config)

from app_package import routes

