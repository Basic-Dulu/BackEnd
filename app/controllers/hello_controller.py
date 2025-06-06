from flask import Blueprint, jsonify
from app.models.skincare_category import SkinCareCategory
from collections import OrderedDict

hello_bp = Blueprint("hello", __name__, url_prefix="/hello")


@hello_bp.route("/laura", methods=["GET"])
def hello_laura():
    """
    A simple Hello World endpoint.
    ---
    responses:
        200:
            description: Returns a hello message
            examples:
                application/json: { "message": "Hello, (name person)!" }
    """
    return jsonify(message="Hello, Laura!")


@hello_bp.route("/fatih", methods=["GET"])
def hello_fatih():
    """
    A simple Hello World endpoint.
    ---
    responses:
        200:
            description: Returns a hello message
            examples:
                application/json: { "message": "Hello, (name person)!" }
    """
    return jsonify(message="Hello, Fatih!")


@hello_bp.route("/", methods=["GET"])
def get_skin_categories():
    skin_categories = [
        skin_category.to_dict()
        for skin_category in SkinCareCategory.query.order_by(
            SkinCareCategory.id.asc()
        ).all()
    ]

    response = OrderedDict(
        [
            ("success", True),
            ("message", "Data fetched successfully"),
            ("data", skin_categories),
        ]
    )

    return jsonify(response)
