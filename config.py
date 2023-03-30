#config file
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'sjaak-swart'

    #location of application database
    #old db SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'postgres://gyfciamwompjgs:8c2edf264454c55673942dee19837e8b9bf8a695588c4c550c74883ef8a2cee2@ec2-34-226-11-94.compute-1.amazonaws.com:5432/daclc0hj770lnq'

    #do not signal the application every time a db change is about to be made
    SQLALCHEMY_TRACK_MODIFICATIONS = False
