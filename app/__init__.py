from flask import Flask
from flasgger import Swagger
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Swagger
    Swagger(app)

    # Register all blueprints
    from app.routes import register_blueprints
    register_blueprints(app)

    return app