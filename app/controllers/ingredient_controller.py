from flask import Blueprint, jsonify, request
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


@ingredient_bp.route("/mix-match", methods=["POST"])
def mix_match():
    data = request.get_json()
    ingredient_one = data.get("ingredient_one")
    ingredient_two = data.get("ingredient_two")

    if not ingredient_one or not ingredient_two:
        return (
            jsonify({"success": False, "message": "Both ingredients are required"}),
            400,
        )

    # Fetch both ingredients by name
    ing1 = Ingredient.query.filter_by(name=ingredient_one).first()
    ing2 = Ingredient.query.filter_by(name=ingredient_two).first()

    if not ing1 or not ing2:
        return (
            jsonify({"success": False, "message": "One or both ingredients not found"}),
            404,
        )

    type1 = ing1.ingredient_type.name if ing1.ingredient_type else None
    type2 = ing2.ingredient_type.name if ing2.ingredient_type else None

    if not type1 or not type2:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "One or both ingredients don't have a type assigned",
                }
            ),
            400,
        )

    # Mix-match logic
    combination = sorted([type1.lower(), type2.lower()])  # ensure consistent ordering

    if combination == ["keras", "keras"]:
        result = "Dangerous"
    elif "keras" in combination and "lembut" in combination:
        result = "Use Mindfully"
    elif combination == ["lembut", "lembut"]:
        result = "Safe"
    else:
        result = "Unknown combination"

    return jsonify(
        {
            "success": True,
            "ingredient_one": {"name": ing1.name, "type": type1},
            "ingredient_two": {"name": ing2.name, "type": type2},
            "result": result,
        }
    )
