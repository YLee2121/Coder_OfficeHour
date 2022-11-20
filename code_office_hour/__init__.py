from flask import Flask

def create_app():

    app = Flask(__name__)

    from .view import view
    from .admin import admin
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/admin')
    
    return app