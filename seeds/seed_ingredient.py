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
            image="niacinamide.png",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=2,  # Kulit Kombinasi
        ),
        Ingredient(
            name="Salicylic Acid",
            description="Salicylic Acid adalah asam beta-hidroksi yang mampu menembus pori-pori dan membersihkan sel kulit mati serta jerawat.",
            image="niacinamide.png",
            benefit="Mengatasi Jerawat, Membersihkan Pori, Mengurangi Peradangan, Mengangkat Sel Kulit Mati",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        Ingredient(
            name="Hyaluronic Acid",
            description="Hyaluronic Acid membantu menghidrasi dan melembapkan kulit, menjadikannya tampak lebih kenyal dan sehat.",
            image="niacinamide.png",
            benefit="Melembapkan Kulit, Mengurangi Kerutan Halus, Meningkatkan Elastisitas Kulit",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=3,  # Kulit Kering
        ),
        Ingredient(
            name="Retinol",
            description="Retinol adalah bentuk vitamin A yang membantu regenerasi kulit, mengurangi kerutan, dan menyamarkan noda hitam.",
            image="niacinamide.png",
            benefit="Mengurangi Tanda Penuaan, Menghaluskan Kulit, Meratakan Warna Kulit",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        Ingredient(
            name="Centella Asiatica",
            description="Centella Asiatica atau daun pegagan dikenal karena sifatnya yang menenangkan dan mempercepat penyembuhan kulit.",
            image="niacinamide.png",
            benefit="Menenangkan Kulit, Menyembuhkan Luka, Mengurangi Kemerahan",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=4,  # Kulit Normal
        ),
        Ingredient(
            name="AHA (Alpha Hydroxy Acid)",
            description="AHA adalah kelompok asam yang larut dalam air dan bekerja di permukaan kulit untuk membantu eksfoliasi sel kulit mati.",
            image="niacinamide.png",
            benefit="Mencerahkan Kulit, Menghaluskan Tekstur Kulit, Mengurangi Noda Hitam, Meratakan Warna Kulit",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        Ingredient(
            name="BHA (Beta Hydroxy Acid)",
            description="BHA merupakan asam yang larut dalam minyak dan efektif untuk membersihkan pori-pori serta mengurangi jerawat dan komedo.",
            image="niacinamide.png",
            benefit="Membersihkan Pori, Mengurangi Jerawat, Mengontrol Minyak, Mengangkat Sel Kulit Mati",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
    ]

    db.session.add_all(ingredients)
    db.session.commit()
    print("✅ Ingredients seeded successfully.")
