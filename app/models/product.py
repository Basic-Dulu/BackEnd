from app.extensions import db
from flask import request


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    suitable_for = db.Column(db.Text, nullable=True)
    key_ingredient = db.Column(db.Text, nullable=True)
    benefit = db.Column(db.Text, nullable=True)

    product_category_id = db.Column(
        db.Integer, db.ForeignKey("product_categories.id"), nullable=False
    )
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"), nullable=False)
    product_type_detail_id = db.Column(
        db.Integer, db.ForeignKey("product_type_details.id"), nullable=True
    )
    ingredient_id = db.Column(
        db.Integer, db.ForeignKey("ingredients.id"), nullable=True
    )
    skin_problem_id = db.Column(
        db.Integer, db.ForeignKey("skin_problems.id"), nullable=True
    )

    # Relationships
    product_category = db.relationship("ProductCategory", backref="products")
    brand = db.relationship("Brand", backref="products")
    skin_problem = db.relationship("SkinProblem", backref="products", lazy="joined")

    def to_dict(self):
        base_url = request.host_url.rstrip("/")

        return {
            "id": self.id,
            "brand": (
                {
                    "id": self.brand.id,
                    "name": self.brand.name,
                }
            ),
            "name": self.name,
            "image": f"{base_url}/static/uploads/{self.image}" if self.image else None,
            "product_category": (
                {
                    "id": self.product_category.id,
                    "description": self.product_category.description,
                }
            ),
            "suitable_for": self.suitable_for,
            "key_ingredient": self.key_ingredient,
            "benefit": self.benefit,
        }
