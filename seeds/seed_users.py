from app.models.user import User
from app import db

def seed_users():
    if User.query.first():
        print("✅ Users already seeded. Skipping.")
        return

    users = [
        User(username="Putri Laura", email="putri@example.com"),
        User(username="Ten Ten TENNNN", email="tententennnnnn@example.com"),
        User(username="faith is Fatih", email="faith@binus.ac.id"),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("✅ Users seeded successfully.")