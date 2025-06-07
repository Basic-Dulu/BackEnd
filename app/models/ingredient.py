from app.extensions import db


class Ingredient(db.Model):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    benefit = db.Column(db.Text, nullable=True)

    ingredient_type_id = db.Column(
        db.Integer, db.ForeignKey("ingredient_types.id"), nullable=True
    )

    # Relatinoship
    ingredient_type = db.relationship(
        "IngredientType", backref="ingredients", lazy="joined"
    )
    products = db.relationship("Product", backref="ingredient", lazy="dynamic")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
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
