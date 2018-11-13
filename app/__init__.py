from flask import Flask
import configparser

app = Flask(__name__)
#from .views import *

conf = configparser.RawConfigParser()
conf.read("../instance/config.py")
print(conf.get("FirstClass", "par1"))
from flask import Flask

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

from .views import *
config.py
class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

