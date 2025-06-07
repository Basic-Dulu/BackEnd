from app.extensions import db
from app.models.ingredient_type import IngredientType


def seed_ingredient_types():
    if IngredientType.query.first():
        print("✅ Ingredient Types already seeded. Skipping.")
        return

    ingredient_types = [
        IngredientType(name="Lembut"),
        IngredientType(name="Keras"),
    ]

    db.session.add_all(ingredient_types)
    db.session.commit()
    print("✅ Ingredient Types seeded successfully.")
