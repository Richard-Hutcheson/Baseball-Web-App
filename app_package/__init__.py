from flask import Flask

app = Flask(__name__)

from app_package import routes

from flask import render_template