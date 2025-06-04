from app.extensions import db


class ProductCategory(db.Model):
    __tablename__ = "product_categories"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)

    # Relationship to Product, changed backref to avoid conflict
    # products = db.relationship(
    #     "Product", backref="category", cascade="all, delete-orphan"
    # )
