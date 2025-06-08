from run import create_app
from app.extensions import db

# Import all seed functions
from seeds import (
    seed_users,
    seed_brands,
    seed_product_categories,
    seed_products,
    seed_skincare_categories,
    seed_product_types,
    seed_product_type_details,
    seed_ingredient_types,
    seed_ingredients,
    seed_skin_test_results,
    seed_skin_test_options,
    seed_skin_test_questions,
    seed_skin_problems,
)


def run_seeds():
    app = create_app()
    with app.app_context():
        db.create_all()

        print("🌱 Seeding database...")

        seed_functions = [
            seed_brands,
            seed_product_categories,
            seed_skincare_categories,
            seed_product_types,
            seed_product_type_details,
            seed_ingredient_types,
            seed_skin_test_results,
            seed_users,
            seed_ingredients,
            seed_skin_problems,
            seed_products,
            seed_skin_test_questions,
            seed_skin_test_options,
        ]

        for seed in seed_functions:
            seed()

        print("✅ Done seeding!")


if __name__ == "__main__":
    run_seeds()
