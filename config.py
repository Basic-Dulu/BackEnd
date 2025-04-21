import os
class Config:
    SWAGGER = {
        "title": "Basic-Dulu API",
        "uiversion": 3,
        "description": "API documentation for Basic-Dulu",
    }

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI",
        "mysql+mysqlconnector://root:admin@localhost:3306/basic_dulu_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False