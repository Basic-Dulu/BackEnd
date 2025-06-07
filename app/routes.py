from app.controllers.hello_controller import hello_bp
from app.controllers.user_controller import user_bp
from app.controllers.upload_controller import upload_bp
from app.controllers.skincare_category_controller import skincare_category_bp
from app.controllers.product_controller import product_bp
from app.controllers.ingredient_controller import ingredient_bp
from app.controllers.skin_test_result_controller import skin_test_result_bp
from app.controllers.skin_test_question_controller import skin_test_question_bp


def register_blueprints_routes(app):
    print("Registering hello_bp...")
    app.register_blueprint(hello_bp)

    print("Registering user_bp...")
    app.register_blueprint(user_bp)

    print("Registering upload_bp...")
    app.register_blueprint(upload_bp)

    print("Registering skincare_category_bp...")
    app.register_blueprint(skincare_category_bp)

    print("Registering product_bp...")
    app.register_blueprint(product_bp)

    print("Registering ingredient_bp...")
    app.register_blueprint(ingredient_bp)

    print("Registering skin_test_result_bp...")
    app.register_blueprint(skin_test_result_bp)

    print("Registering skin_test_question_bp...")
    app.register_blueprint(skin_test_question_bp)
