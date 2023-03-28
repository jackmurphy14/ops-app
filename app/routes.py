#routes file
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
