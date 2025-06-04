from app.extensions import db
from app.models.brand import Brand


def seed_brands():
    if Brand.query.first():
        print("✅ Brands already seeded. Skipping.")
        return

    brands = [
        Brand(name="Somethinc"),
        Brand(name="Erha"),
        Brand(name="Facetology"),
    ]

    db.session.add_all(brands)
    db.session.commit()
    print("✅ Brands seeded successfully.")
