from flask import Blueprint

api = Blueprint('app',__name__,template_folder='templates')

from . import views,email