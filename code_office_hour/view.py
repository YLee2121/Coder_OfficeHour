from flask import Blueprint

view = Blueprint('view', __name__)

@view.route('/')
def home():
    return 'code office hour'

@view.route('/register')
def register():
    return 'register'
