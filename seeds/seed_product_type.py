from app.extensions import db
from app.models.product_type import ProductType


def seed_product_types():
    if ProductType.query.first():
        print("✅ Product Types already seeded. Skipping.")
        return

    product_types = [
        # 1
        ProductType(name="Cleansing Balm"),
        # 2
        ProductType(name="Cleansing Milk"),
        # 3
        ProductType(name="Cleansing Oil"),
        # 4
        ProductType(name="Micellar Water"),
        # 5
        ProductType(name="Cream Cleanser"),
        # 6
        ProductType(name="Gel Cleanser"),
        # 7
        ProductType(name="Foaming Cleanser"),
        # 8
        ProductType(name="Gel Moisturizer"),
        # 9
        ProductType(name="Cream Moisturizer"),
        # 10
        ProductType(name="Physical Sunscreen"),
        # 11
        ProductType(name="Chemical Sunscreen"),
        # 12
        ProductType(name="Hybrid Sunscreen"),
    ]

    db.session.add_all(product_types)
    db.session.commit()
    print("✅ Product Types seeded successfully.")
