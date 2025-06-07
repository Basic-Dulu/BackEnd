from app.extensions import db


class SkinTestOption(db.Model):
    __tablename__ = "skin_test_options"

    id = db.Column(db.Integer, primary_key=True)
    option = db.Column(db.Text, nullable=False)
    point = db.Column(db.Integer, nullable=False)

    question_id = db.Column(
        db.Integer, db.ForeignKey("skin_test_questions.id"), nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "option": self.option,
            "point": self.point,
        }
