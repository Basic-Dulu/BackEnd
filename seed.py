from app import create_app, db
from seeds.seed_users import seed_users
# from seeds.seed_posts import seed_posts (when you make it)

app = create_app()

with app.app_context():
    db.create_all()

    print("🌱 Seeding database...")
    seed_users()
    # seed_posts()
    print("🌱 Done seeding!")