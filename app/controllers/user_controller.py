from flask import Blueprint, request, jsonify, current_app
from app.models.user import User, db
from app.models.skin_test_result import SkinTestResult
from collections import OrderedDict
from werkzeug.utils import secure_filename

import jwt
import datetime
import os

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def get_users():
    users = [user.to_dict() for user in User.query.order_by(User.id.asc()).all()]

    response = OrderedDict(
        [("success", True), ("message", "Data fetched successfully"), ("data", users)]
    )

    return jsonify(response)


@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"success": False, "message": "Missing or Invalid token"}), 401

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"success": False, "message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"success": False, "message": "Invalid token"}), 401

    if payload["user_id"] != user_id:
        return jsonify({"success": False, "message": "Unauthorized access"}), 403

    user = User.query.get(payload["user_id"])

    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    return (
        jsonify({"success": True, "message": "User found", "data": user.to_dict()}),
        200,
    )


# for create new user
@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.get_json()
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    gender = data.get("gender")

    # check if the it's filled or not
    if not email:
        return (
            jsonify({"succes": False, "message": "email are required!"}),
            400,
        )

    if not username:
        return (
            jsonify({"succes": False, "message": "username are required!"}),
            400,
        )

    if not password:
        return (
            jsonify({"succes": False, "message": "password are required!"}),
            400,
        )

    if not gender:
        return (
            jsonify({"succes": False, "message": "gender are required!"}),
            400,
        )

    # check if email already exist or not
    if User.query.filter_by(email=email).first():
        return jsonify({"succes": False, "message": "email already exist!"}), 409

    if User.query.filter_by(username=username).first():
        return jsonify({"succes": False, "message": "username already exist!"}), 409

    # the inputted save into the db
    if gender.lower() == "male":
        new_user = User(
            email=email,
            username=username,
            password=password,
            gender=gender,
            image="user-male.png",
        )
    elif gender.lower() == "female":
        new_user = User(
            email=email,
            username=username,
            password=password,
            gender=gender,
            image="user-female.png",
        )
    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            {
                "succes": True,
                "message": "user succesfully registered!",
                "user": new_user.username,
            }
        ),
        201,
    )


# for login
@user_bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return (
            jsonify({"succes": False, "message": "email and password are required!"}),
            400,
        )

    found_user = User.query.filter_by(email=email).first()

    if not found_user or found_user.password != password:
        return jsonify({"success": False, "message": "Email or Password is Invalid!"})

    token = jwt.encode(
        {
            "user_id": found_user.id,
            "user_name": found_user.username,
            "exp": datetime.datetime.now() + datetime.timedelta(hours=1),
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    return (
        jsonify(
            {
                "succes": True,
                "message": "Login Successfull",
                "token": token,
            }
        ),
        200,
    )


@user_bp.route("/<int:user_id>/skin-test", methods=["PUT"])
def assign_skin_test_result(user_id):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"success": False, "message": "Missing or Invalid token"}), 401

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"success": False, "message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"success": False, "message": "Invalid token"}), 401

    if payload["user_id"] != user_id:
        return jsonify({"success": False, "message": "Unauthorized access"}), 403

    user = User.query.get(user_id)
    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    data = request.get_json()
    score = data.get("score")
    if score is None:
        return jsonify({"success": False, "message": "Score is required"}), 400

    skin_test_result = SkinTestResult.query.filter(
        SkinTestResult.min_score <= score, SkinTestResult.max_score >= score
    ).first()

    if not skin_test_result:
        return (
            jsonify(
                {
                    "success": False,
                    "message": "No matching skin test result found for the score",
                }
            ),
            404,
        )

    user.skin_test_result_id = skin_test_result.id
    db.session.commit()

    return (
        jsonify(
            {
                "success": True,
                "message": "Skin test result assigned successfully",
                "data": user.to_dict(),
            }
        ),
        200,
    )


@user_bp.route("/<int:user_id>/skin-test-result", methods=["GET"])
def get_user_skin_test_result(user_id):
    # Extract token from Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"success": False, "message": "Missing or Invalid token"}), 401

    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return jsonify({"success": False, "message": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"success": False, "message": "Invalid token"}), 401

    # Ensure the authenticated user is the same as the one being requested
    if payload["user_id"] != user_id:
        return jsonify({"success": False, "message": "Unauthorized access"}), 403

    user = User.query.get(user_id)

    if not user:
        return jsonify({"success": False, "message": "User not found"}), 404

    if not user.skin_test_result:
        return (
            jsonify({"success": False, "message": "User has no skin test result"}),
            404,
        )

    # Convert the skin test result to dict
    result_data = user.skin_test_result.to_dict()

    # Inject the user's image URL manually
    base_url = request.host_url.rstrip("/")
    result_data["user_image"] = (
        f"{base_url}/static/uploads/{user.image}" if user.image else None
    )

    return (
        jsonify(
            {
                "success": True,
                "message": "Skin test result retrieved successfully",
                "data": result_data,
            }
        ),
        200,
    )
