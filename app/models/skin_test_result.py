from app.extensions import db


class SkinTestResult(db.Model):
    __tablename__ = "skin_test_results"

    id = db.Column(db.Integer, primary_key=True)
    min_score = db.Column(db.Integer, nullable=False)
    max_score = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    characteristics = db.Column(db.Text, nullable=True)
    dos = db.Column(db.Text, nullable=True)
    donts = db.Column(db.Text, nullable=True)

    # Relationship
    ingredients = db.relationship(
        "Ingredient", backref="skin_test_result", lazy="dynamic"
    )

    def to_dict(self):
        return {
            "id": self.id,
            "score_range": f"{self.min_score}-{self.max_score}",
            "name": self.name,
            "description": self.description,
            "characteristicss": (
                [char.strip() for char in self.characteristics.split("; ")]
                if self.characteristics
                else []
            ),
            "dos": self.dos,
            "donts": self.donts,
            "recommend_ingredients": [
                ingredient.to_dict() for ingredient in self.ingredients.all()
            ],
        }
