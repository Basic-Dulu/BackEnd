from app.extensions import db
from flask import request


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=False)
    benefit = db.Column(db.Text, nullable=True)

    ingredient_type_id = db.Column(
        db.Integer, db.ForeignKey("ingredient_types.id"), nullable=True
    )
    skin_test_result_id = db.Column(
        db.Integer, db.ForeignKey("skin_test_results.id"), nullable=True
    )

    # Relatinoship
    ingredient_type = db.relationship(
        "IngredientType", backref="ingredients", lazy="joined"
    )
    products = db.relationship("Product", backref="ingredient", lazy="dynamic")

    def to_dict(self):
        base_url = request.host_url.rstrip("/")

        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "image": f"{base_url}/static/uploads/{self.image}" if self.image else None,
            "ingredient_type": (
                {
                    "id": self.ingredient_type.id,
                    "name": self.ingredient_type.name,
                }
                if self.ingredient_type
                else None
            ),
            "benefits": (
                [b.strip() for b in self.benefit.split(", ")] if self.benefit else []
            ),
            "products": [product.to_dict() for product in self.products.all()],
        }
