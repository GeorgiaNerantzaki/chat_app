from flask import Blueprint
#authentication blueprint
bp = Blueprint('auth',__name__)

from app.auth import routes