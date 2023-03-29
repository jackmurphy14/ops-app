from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from app.models import User

#defines user login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#defines registration form
class RegistrationForm(FlaskForm):
    first_name = StringField('Enter your forename: ', validators=[DataRequired()])
    last_name = StringField('Enter your surname: ', validators=[DataRequired()])
    username = StringField('Create a username: ', validators=[DataRequired()])
    password = PasswordField('Create a password: ', validators=[DataRequired()])
    password2 = PasswordField('Repeat your password: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already taken')