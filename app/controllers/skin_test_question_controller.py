from flask import Blueprint, jsonify
from app.models.skin_test_question import SkinTestQuestion

skin_test_question_bp = Blueprint(
    "skin_test_question", __name__, url_prefix="/skin-test-questions"
)


@skin_test_question_bp.route("/", methods=["GET"])
def get_all_skin_test_questions():
    questions = SkinTestQuestion.query.all()
    return jsonify([q.to_dict() for q in questions]), 200


@skin_test_question_bp.route("/<int:question_id>", methods=["GET"])
def get_skin_test_question_by_id(question_id):
    question = SkinTestQuestion.query.get(question_id)
    if not question:
        return jsonify({"error": "Question not found"}), 404
    return jsonify(question.to_dict()), 200
