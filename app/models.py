from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(40))
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    admin = db.Column(db.String(1), default="F")

    #for python interpreter
    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        return self.admin == "T"
    
    def make_admin(self):
        self.admin = "T"

    def remove_admin(self):
        self.admin = "F"

#this function loads a user when given the id
@login.user_loader
def load_user(id):
    return User.query.get(int(id))