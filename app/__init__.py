from flask import Flask
from config import Config 

#creating the application object as an instance of class Flask
app = Flask(__name__)

#tells Flask to read and apply config file
app.config.from_object(Config)

from app import routes