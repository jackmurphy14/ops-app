#config file
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sjaak-swart'

    #location of application database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')

    #do not signal the application every time a db change is about to be made
    SQLALCHEMY_TRACK_MODIFICATIONS = False
