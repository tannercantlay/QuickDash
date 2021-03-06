from flask import Flask, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from werkzeug.utils import secure_filename
import bitpay
from bitpay.client import Client

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'quickdashugahacks@gmail.com',
    MAIL_PASSWORD = 'inferno4lyfe',
    SECRET_KEY = 'any secret string',
    ENVIRONMENT = 'development'
    ))
mail = Mail(app)

client = Client('https://test.bitpay.com') #bitpay.config.json
from app import routes, models,key_utils
