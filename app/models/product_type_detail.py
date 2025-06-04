from app.extensions import db


class ProductTypeDetail(db.Model):
    __tablename__ = "product_type_details"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=True)

    product_type_id = db.Column(
        db.Integer, db.ForeignKey("product_types.id"), nullable=False
    )

    skincare_category_id = db.Column(
        db.Integer, db.ForeignKey("skincare_categories.id"), nullable=False
    )

    # products = db.relationship(
    #     "Product", backref="product_type", cascade="all, delete-orphan"
    # )
