from run import create_app
from app.extensions import db
from seeds.seed_users import seed_users
from seeds.seed_brands import seed_brands
from seeds.seed_product_category import seed_product_categories
from seeds.seed_products import seed_products
from seeds.seed_skincare_category import seed_skincare_categories
from seeds.seed_product_type import seed_product_types
from seeds.seed_product_type_detail import seed_product_type_details
from seeds.seed_ingredient_type import seed_ingredient_types
from seeds.seed_ingredient import seed_ingredients

# from seeds.seed_posts import seed_posts (when you make it)

app = create_app()

with app.app_context():
    db.create_all()

    print("🌱 Seeding database...")
    seed_users()
    seed_brands()
    seed_product_categories()
    seed_skincare_categories()
    seed_product_types()
    seed_product_type_details()
    seed_ingredient_types()
    seed_ingredients()
    seed_products()

    print("🌱 Done seeding!")
