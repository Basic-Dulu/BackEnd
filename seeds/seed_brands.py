from app.extensions import db
from app.models.brand import Brand


def seed_brands():
    if Brand.query.first():
        print("✅ Brands already seeded. Skipping.")
        return

    brands = [
        # 1
        Brand(name="Somethinc"),
        # 2
        Brand(name="Facetology"),
        # 3
        Brand(name="Whitelab"),
        # 4
        Brand(name="BIYU"),
        # 5
        Brand(name="Hyalupure"),
        # 6
        Brand(name="Dear Me Beauty"),
        # 7
        Brand(name="Viva"),
        # 8
        Brand(name="Teratu"),
        # 9
        Brand(name="Bio Beauty Lab"),
        # 10
        Brand(name="Hyalupre"),
        # 11
        Brand(name="True To Skin"),
        # 12
        Brand(name="Labore"),
        # 13
        Brand(name="Skintheory"),
        # 14
        Brand(name="Oasea"),
        # 15
        Brand(name="ERHA"),
        # 16
        Brand(name="From This Island"),
        # 17
        Brand(name="Avoskin"),
        # 18
        Brand(name="Wardah"),
        # 19
        Brand(name="Azarine"),
        # 20
        Brand(name="Glamazing"),
        # 21
        Brand(name="Emina"),
        # 22
        Brand(name="NPure"),
        # 23
        Brand(name="Tavi"),
        # 24
        Brand(name="Skin Game"),
        # 25
        Brand(name="Amaterasun"),
        # 26
        Brand(name="HALE"),
        # 27
        Brand(name="Carasun"),
        # 28
        Brand(name="Acnaway"),
        # 29
        Brand(name="For Skin's Sake FSS"),
        # 30
        Brand(name="Jarte"),
        # 31
        Brand(name="Harlette"),
        # 32
        Brand(name="ElsheSkin"),
        # 33
        Brand(name="Dermies by ERHA"),
        # 34
        Brand(name="Better Botanics"),
        # 35
        Brand(name="Studio Tropik"),
        # 36
        Brand(name="MS Glow"),
    ]

    db.session.add_all(brands)
    db.session.commit()
    print("✅ Brands seeded successfully.")
