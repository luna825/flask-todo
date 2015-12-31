from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)

    from .todo import app as app_blueprint
    app.register_blueprint(app_blueprint)
    
    return app
