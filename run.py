from flask_migrate import Migrate
from Fahead import db,app

migrate = Migrate(app,db)
