from flask import Blueprint, make_response
from app.models.user import User

import json

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
    users = [user.to_dict() for user in User.query.order_by(User.id.asc()).all()]
    return make_response(json.dumps({"users": users}, indent=4), 200)