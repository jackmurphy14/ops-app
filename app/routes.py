#routes file
from flask import render_template, Flask
from app.forms import LoginForm

app = Flask(__name__)
@app.route('/')
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
