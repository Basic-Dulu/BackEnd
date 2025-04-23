from flask import Flask
from flasgger import Swagger
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Swagger
    db.init_app(app)
    Swagger(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


    # Register all blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app