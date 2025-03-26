from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)  # Initialize Swagger

@app.route('/putri-laura', methods=['GET'])
def hello():
    """
    A simple Hello World endpoint.
    ---
    responses:
      200:
        description: Returns a hello message
        examples:
          application/json: { "message": "Hello, World!" }
    """
    return jsonify(message="Hello, Putri Laura Cantik!")

if __name__ == '__main__':
    app.run(debug=True)
