from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/putri-laura', methods=['GET'])
def hello():
    """
    A simple Hello World endpoint.
    ---
    responses:
        00:
            description: Returns a hello message
            examples:
                application/json: { "message": "Hello, Test!" }
    """
    return jsonify(message="Hello, Test!")