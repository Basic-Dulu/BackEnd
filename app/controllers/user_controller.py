from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    """
    Get all users.
    ---
    responses:
        200:
            description: A list of users
            examples:
                pplication/json: { "users": ["Putri", "Laura", "Alzam"] }
    """
    users = ["Putri", "Laura", "Wadidaw"]
    return jsonify(users=users)