from flask import Blueprint, request, jsonify
from app.models.user import User, db
from collections import OrderedDict

user_bp = Blueprint("user", __name__, url_prefix="/users")


@user_bp.route("/", methods=["GET"])
def get_users():
    """
    Get all users.
    ---
    responses:
        200:
            description: A list of users
            examples:
                application/json: { "users": [{"id": 1, "username": "Putri", "email": "putri@example.com"}] }
    """
    users = [user.to_dict() for user in User.query.order_by(User.id.asc()).all()]

    response = OrderedDict(
        [("success", True), ("message", "Data fetched successfully"), ("data", users)]
    )

    return jsonify(response)


# for create new user
@user_bp.route("/", methods=["POST"])
def create_user():
    """
    Create a new user.
    ---
    tags:
        - Users
    parameters:
      - in: body
        name: body
        required: true
        schema:
          id: User
          required:
            - username
            - email
          properties:
            email:
                type: string
                example: putri@example.com
            username:
              type: string
              example: putri
            password:
              type: string
              example: passwordexample123
            gender:
              type: string
              example: Female
    responses:
      201:
        description: User created successfully
      400:
        description: Invalid input
      409:
        description: Email already exists
      409:
        description: Username already exists
    """

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
    new_user = User(email=email, username=username, password=password, gender=gender)
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
