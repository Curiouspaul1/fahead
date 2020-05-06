from flask_migrate import Migrate
from models import User
from Fahead import db,app,mail

migrate = Migrate(app,db)

@app.shell_context_processor
def make_shell_context():
    return dict(app=app,User=User,mail=mail)
