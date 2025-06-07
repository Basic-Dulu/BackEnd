from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)

    skin_test_result_id = db.Column(
        db.Integer, db.ForeignKey("skin_test_results.id"), nullable=True
    )

    # Relationship
    # The backref name skin_test_results suggests a list of SkinTestResult, but since it’s a one-to-many relationship from SkinTestResult to User, the backref on SkinTestResult will be users.

    # wrong
    # skin_test_result = db.relationship(
    #     "SkinTestResult", backref="skin_test_results", lazy="joined"
    # )

    # correct
    skin_test_result = db.relationship("SkinTestResult", backref="users", lazy="joined")

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "gender": self.gender,
            "skin_test_result": (
                {
                    "id": self.skin_test_result.id,
                    "name": self.skin_test_result.name,
                }
                if self.skin_test_result
                else None
            ),
        }
