from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from .config import config
from flask_mail import Mail, Message
import os


app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV') or 'default'])

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)

# register blueprints
from .main import api
app.register_blueprint(api,url_prefix='/api')