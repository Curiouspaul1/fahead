from flask import Blueprint

api = Blueprint('app',__name__)

from . import views