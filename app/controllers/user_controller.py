from flask import Blueprint, make_response, jsonify
from app.models.user import User
from collections import OrderedDict

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

    response = OrderedDict()
    response["success"] = True
    response["message"] = "Data fetched successfully"
    response["data"] = users
    # return make_response(json.dumps({"users": users}, indent=4), 200)
    # return jsonify({
    #     "success": True,
    #     "message": "Users fetched successfully",
    #     "data": users
    # })
    return jsonify(response)