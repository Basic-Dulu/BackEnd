from app.controllers.hello_controller import hello_bp
from app.controllers.user_controller import user_bp  # ⬅️ new import

def register_blueprints(app):
    app.register_blueprint(hello_bp)
    app.register_blueprint(user_bp)  # ⬅️ register new blueprint