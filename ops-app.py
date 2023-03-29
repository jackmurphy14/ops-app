#defines the Flask application instance
from app import app, db
from app.models import User

#python interpreter in context of application
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}