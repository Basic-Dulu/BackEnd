from flask import Blueprint, jsonify
from app.models import SkinTestResult

skin_test_result_bp = Blueprint(
    "skin_test_result", __name__, url_prefix="/skin-test-results"
)


# Get all skin test results
@skin_test_result_bp.route("/", methods=["GET"])
def get_all_skin_test_results():
    results = SkinTestResult.query.all()
    return jsonify([result.to_dict() for result in results]), 200


# Get a single skin test result by ID
@skin_test_result_bp.route("/<int:result_id>", methods=["GET"])
def get_skin_test_result_by_id(result_id):
    result = SkinTestResult.query.get(result_id)
    if not result:
        return jsonify({"success": False, "message": "Skin test result not found"}), 404

    return jsonify(result.to_dict()), 200

