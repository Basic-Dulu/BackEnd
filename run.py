from dotenv import load_dotenv
load_dotenv()
from flask import jsonify, Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from app.extensions import db
from app.routes import register_blueprints_routes
from flask_cors import CORS
from config import Config
import os

def create_app():
    app = Flask(__name__)
    app.json.sort_keys = False

    # load_dotenv()

    app.config.from_object(Config)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"

    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Access API"}
    )
    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

    @app.route("/")
    def home():
        return jsonify({"Message": "app up and running successfully"})

    db.init_app(app)

    # CORS setup to allow only your frontend URL
    # CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
    # CORS(app, resources={r"/*": {"origins": ["https://basic-dulu-flask.vercel.app"]}})
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)


    # Register all blueprints
    register_blueprints_routes(app)

    # Handle preflight CORS request
    @app.route("/users", methods=["OPTIONS"])
    def options():
        return "", 200

    return app

# Create the app instance for Gunicorn
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
