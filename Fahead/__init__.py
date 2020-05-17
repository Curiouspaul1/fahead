from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import config
from flask_mail import Mail, Message
from flask_cors import CORS
import os
import logging


app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV') or 'default'])

db = SQLAlchemy(app)
ma = Marshmallow(app)
mail = Mail(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
logging.getLogger('flask_cors').level = logging.DEBUG

# register blueprints
from .main import api
app.register_blueprint(api,url_prefix='/api')