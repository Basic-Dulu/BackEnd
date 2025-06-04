from app.extensions import db
from app.models.product_type import ProductType


def seed_product_types():
    if ProductType.query.first():
        print("✅ Product Types already seeded. Skipping.")
        return

    product_types = [
        ProductType(name="Gel Moisturizer"),
        ProductType(name="Cream Moisturizer"),
        ProductType(name="Oil-based Moisturizer"),
    ]

    db.session.add_all(product_types)
    db.session.commit()
    print("✅ Product Types seeded successfully.")
