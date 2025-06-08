from app.extensions import db


class SkinProblem(db.Model):
    __tablename__ = "skin_problems"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    saw_point = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "saw_point": self.saw_point,
        }
