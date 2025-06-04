from app.extensions import db


class SkinCareCategory(db.Model):
    __tablename__ = "skincare_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slogan = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    benefit = db.Column(db.Text, nullable=True)
    how_to_use = db.Column(db.Text, nullable=True)

    # # Many-to-many relationship with Benefit through the SkinCareCategoryBenefit table
    # benefits = db.relationship(
    #     "Benefit",
    #     secondary="skincare_category_benefits",
    #     backref=db.backref(
    #         "categories", lazy="dynamic"
    #     ),  # Changed backref to "categories"
    #     # Removed delete-orphan here
    # )

    # # One-to-many relationship with ProductType
    # product_types = db.relationship(
    #     "ProductType",
    #     backref="category",
    #     cascade="all, delete-orphan",  # Changed backref to "category"
    # )
