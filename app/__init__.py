from flask import Flask, send_from_directory
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()


def create_app():
    load_dotenv()

    app = Flask(__name__, static_folder="app/static")
    app.config.from_object(Config)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    SWAGGER_URL = "/swagger"  # URL prefix to access docs
    API_URL = "/static/swagger.json"  # Swagger spec location

    swagger_bo = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Basic-Dulu API"}
    )
    app.register_blueprint(swagger_bo, url_prefix=SWAGGER_URL)

    @app.route("/static/swagger.json")
    def serve_swagger_spec():
        return send_from_directory(os.getcwd(), "swagger.json")

    # Initialize Swagger
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # Register all blueprints
    from app.routes import register_blueprints

    register_blueprints(app)

    return app
