from flask import Flask
from flask_jsonrps import JSONRPS

app = Flask(__name__)
jsonrps = JSONRPS(app, '/api/')
from views import views