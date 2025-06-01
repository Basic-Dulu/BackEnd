from app.controllers.hello_controller import hello_bp
from app.controllers.user_controller import user_bp  # ⬅️ new import
from app.controllers.upload_controller import upload_bp


def register_blueprints_routes(app):
    app.register_blueprint(hello_bp)
    app.register_blueprint(user_bp)  # ⬅️ register new blueprint
    app.register_blueprint(upload_bp)
