from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    suitable_for = db.Column(db.String(100), nullable=True)
    ingredient = db.Column(db.Text, nullable=True)
    benefit = db.Column(db.Text, nullable=True)

    product_category_id = db.Column(
        db.Integer, db.ForeignKey("product_categories.id"), nullable=False
    )
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"), nullable=False)
    product_type_detail_id = db.Column(
        db.Integer, db.ForeignKey("product_type_details.id"), nullable=True
    )

    # Relationships
    product_category = db.relationship("ProductCategory", backref="products")
    brand = db.relationship("Brand", backref="products")

    def to_dict(self):
        return {
            "id": self.id,
            "brand": (
                {
                    "id": self.brand.id,
                    "name": self.brand.name,
                }
            ),
            "name": self.name,
            "product_category": (
                {
                    "id": self.product_category.id,
                    "description": self.product_category.description,
                }
            ),
            "suitable_for": self.suitable_for,
            "ingredient": self.ingredient,
            "benefit": self.benefit,
        }
