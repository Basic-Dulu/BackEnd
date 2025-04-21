from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__, url_prefix='/hello')

@hello_bp.route('/laura', methods=['GET'])
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

@hello_bp.route('/fatih', methods=['GET'])
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