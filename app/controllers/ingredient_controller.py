from flask import Blueprint, jsonify
from app.models.ingredient import Ingredient

ingredient_bp = Blueprint("ingredient", __name__, url_prefix="/ingredients")


@ingredient_bp.route("/", methods=["GET"])
def get_all_ingredients():
    ingredients = Ingredient.query.all()

    data = [ingredient.to_dict() for ingredient in ingredients]

    return jsonify(
        {"success": True, "message": "Ingredients fetched successfully", "data": data}
    )


@ingredient_bp.route("/<int:ingredient_id>", methods=["GET"])
def get_ingredient_by_id(ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)

    if not ingredient:
        return jsonify({"success": False, "message": "Ingredient not found"}), 404

    return jsonify(
        {
            "success": True,
            "message": "Ingredient fetched successfully",
            "data": ingredient.to_dict(),
        }
    )
