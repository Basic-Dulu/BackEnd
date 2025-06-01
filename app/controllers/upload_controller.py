# app/controllers/file_controller.py
from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename
from app.utils.file import allowed_file

upload_bp = Blueprint("upload", __name__, url_prefix="/upload")


@upload_bp.route("/", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"success": False, "message": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"success": False, "message": "No selected file"}), 400

    if file and allowed_file(file.filename, current_app.config["ALLOWED_EXTENSIONS"]):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(
            current_app.root_path, current_app.config["UPLOAD_FOLDER"]
        )
        os.makedirs(upload_path, exist_ok=True)
        file.save(os.path.join(upload_path, filename))

        file_url = f"/static/uploads/{filename}"
        return (
            jsonify({"success": True, "message": "File uploaded", "url": file_url}),
            201,
        )

    return jsonify({"success": False, "message": "File type not allowed"}), 400
