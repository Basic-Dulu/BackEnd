from app.extensions import db
from app.models.product_category import ProductCategory


def seed_product_categories():
    if ProductCategory.query.first():
        print("✅ Product Categories already seeded. Skipping.")
        return

    product_categories = [
        ProductCategory(description="SPF"),
        ProductCategory(description="Pelembab"),
        ProductCategory(description="Pembersih"),
    ]

    db.session.add_all(product_categories)
    db.session.commit()
    print("✅ Product Categories seeded successfully.")
