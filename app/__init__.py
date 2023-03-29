from flask import Flask
from config import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#creating the application object as an instance of class Flask
app = Flask(__name__)

#tells Flask to read and apply config file
app.config.from_object(Config)

#represents the database
db = SQLAlchemy(app)

#represents migration engine
migrate = Migrate(app, db)

from app import routes, models