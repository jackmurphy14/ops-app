from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, login_required

#creating the application object as an instance of class Flask
app = Flask(__name__)

#tells Flask to read and apply config file
app.config.from_object(Config)

#represents the database
db = SQLAlchemy(app)

#represents migration engine
migrate = Migrate(app, db)

login = LoginManager(app)

#view function that handles logins
login.login_view = 'login'

from app import routes, models