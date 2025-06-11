from flask import Blueprint, jsonify
from app.models.skin_problems import SkinProblem
from collections import OrderedDict

skin_problem_bp = Blueprint("skin_problem", __name__, url_prefix="/skin_problems")


@skin_problem_bp.route("/", methods=["GET"])
def get_skin_problems():
    skin_problems = SkinProblem.query.order_by(SkinProblem.id.asc()).all()
    skin_problem_list = [skin_problem.to_dict() for skin_problem in skin_problems]

    return jsonify(
        {
            "success": True,
            "message": "Skin Problems fetched successfully",
            "data": skin_problem_list,
        }
    )
