import os


class Config:
    # Punya Fatih
    # SQLALCHEMY_DATABASE_URI = os.getenv(
    #     "DATABASE_URI", "mysql+mysqlconnector://root:admin@localhost:3306/basic_dulu_db"
    # )

    # Punya Putri
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = os.path.join("static", "uploads")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
