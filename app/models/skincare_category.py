from app.extensions import db
from flask import request


class SkinCareCategory(db.Model):
    __tablename__ = "skincare_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slogan = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=True)
    image = db.Column(db.String(100), nullable=False)
    benefit = db.Column(db.Text, nullable=True)
    how_to_use = db.Column(db.Text, nullable=True)

    product_type_details = db.relationship(
        "ProductTypeDetail", backref="skincare_category", lazy="dynamic"
    )

    def to_dict(self):
        base_url = request.host_url.rstrip("/")

        return {
            "id": self.id,
            "name": self.name,
            "slogan": self.slogan,
            "description": self.description,
            "image": f"{base_url}/static/uploads/{self.image}" if self.image else None,
            "benefit": self.benefit,
            "how_to_use": (
                [how_to.strip() for how_to in self.how_to_use.split(", ")]
                if self.how_to_use
                else []
            ),
            "product_type_details": [
                detail.to_dict() for detail in self.product_type_details.all()
            ],
        }

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
