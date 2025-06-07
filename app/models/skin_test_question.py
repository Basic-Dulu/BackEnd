from app.extensions import db


class SkinTestQuestion(db.Model):
    __tablename__ = "skin_test_questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)

    skin_test_options = db.relationship(
        "SkinTestOption", backref="skin_test_question", lazy="dynamic"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "options": [option.to_dict() for option in self.skin_test_options.all()],
        }
