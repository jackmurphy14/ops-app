#routes file
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect('/index')
    return render_template('login.html', form=form)

@app.route('/index')
def index():
    return 'Home Page'
