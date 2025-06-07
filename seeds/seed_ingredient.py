from app.extensions import db
from app.models.ingredient import Ingredient


def seed_ingredients():
    if Ingredient.query.first():
        print("✅ Ingredients already seeded. Skipping.")
        return

    ingredients = [
        Ingredient(
            name="Niacinamide",
            description="Niacinamide atau vitamin B3 membantu mencerahkan kulit, memperbaiki elastisitas, dan memperkuat skin barrier.",
            benefit="Mencerahkan Kulit, Memperkuat Skin Barrier, Mengontrol Minyak Berlebih, Mencegah Tanda Penuaan, Mengurangi Peradangan Jerawat",
            ingredient_type_id=1,  # Lembut
        ),
        Ingredient(
            name="Salicylic Acid",
            description="Salicylic Acid adalah asam beta-hidroksi yang mampu menembus pori-pori dan membersihkan sel kulit mati serta jerawat.",
            benefit="Mengatasi Jerawat, Membersihkan Pori, Mengurangi Peradangan, Mengangkat Sel Kulit Mati",
            ingredient_type_id=2,  # Keras
        ),
        Ingredient(
            name="Hyaluronic Acid",
            description="Hyaluronic Acid membantu menghidrasi dan melembapkan kulit, menjadikannya tampak lebih kenyal dan sehat.",
            benefit="Melembapkan Kulit, Mengurangi Kerutan Halus, Meningkatkan Elastisitas Kulit",
            ingredient_type_id=1,  # Lembut
        ),
        Ingredient(
            name="Retinol",
            description="Retinol adalah bentuk vitamin A yang membantu regenerasi kulit, mengurangi kerutan, dan menyamarkan noda hitam.",
            benefit="Mengurangi Tanda Penuaan, Menghaluskan Kulit, Meratakan Warna Kulit",
            ingredient_type_id=2,  # Keras
        ),
        Ingredient(
            name="Centella Asiatica",
            description="Centella Asiatica atau daun pegagan dikenal karena sifatnya yang menenangkan dan mempercepat penyembuhan kulit.",
            benefit="Menenangkan Kulit, Menyembuhkan Luka, Mengurangi Kemerahan",
            ingredient_type_id=1,  # Lembut
        ),
    ]

    db.session.add_all(ingredients)
    db.session.commit()
    print("✅ Ingredients seeded successfully.")
