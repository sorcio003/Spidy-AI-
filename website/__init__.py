from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager, LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dujsdujsddfsdbfjksfjhksdhjkfjh"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    return app