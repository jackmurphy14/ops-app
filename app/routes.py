#routes file
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User
from werkzeug.urls import url_parse


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #prevents logged in users navigating to login section
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        
        #queries database with form submission to find the user
        user = User.query.filter_by(username=form.username.data).first()

        #if user doesn't exist or username entry doesn't match stored password, notify that login attempt has failed
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        #execute function to login user if stored username and password match form entry
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')

#requires users to be logged in to access this page, even if they manually type url
@login_required

def index():
    return render_template('index.html')