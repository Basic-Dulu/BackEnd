from app.extensions import db
from app.models.product_type_detail import ProductTypeDetail


def seed_product_type_details():
    if ProductTypeDetail.query.first():
        print("✅ Product Type Details already seeded. Skipping.")
        return

    product_type_details = [
        ProductTypeDetail(
            description="Ringan, berbahan dasar air, baik untuk kulit berminyak.",
            product_type_id=1,
            skincare_category_id=3,
        ),
        ProductTypeDetail(
            description="Ringan dan mudah dioleskan, cocok untuk digunakan di badan.",
            product_type_id=2,
            skincare_category_id=3,
        ),
        ProductTypeDetail(
            description="Kaya akan minyak, cocok untuk kulit yang sangat kering atau kulit yang sudah tua.",
            product_type_id=3,
            skincare_category_id=3,
        ),
    ]

    db.session.add_all(product_type_details)
    db.session.commit()
    print("✅ Product Type Details seeded successfully.")
