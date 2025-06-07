from app.extensions import db
from app.models.ingredient import Ingredient


def seed_ingredients():
    if Ingredient.query.first():
        print("✅ Ingredients already seeded. Skipping.")
        return

    ingredients = [
        Ingredient(
            name="Niacinamide",
            description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque gravida blandit ex vel eleifend. Donec eros ipsum, sagittis sed nibh sed, placerat laoreet justo. Sed gravida risus sit amet eros feugiat dignissim.",
            benefit="Mencerahkan Kulit, Memperkuat Skin Barrier, Mengontrol Minyak Berlebih, Mencegah Tanda Penuaan, Mengurangi Peradangan Jerawat",
            ingredient_type_id=1,
        )
    ]

    db.session.add_all(ingredients)
    db.session.commit()
    print("✅ Ingredients seeded successfully.")
