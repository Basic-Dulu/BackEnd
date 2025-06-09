from app.models.user import User
from app.extensions import db


def seed_users():
    if User.query.first():
        print("✅ Users already seeded. Skipping.")
        return

    users = [
        User(
            username="Putri Laura",
            email="putri@example.com",
            password="putrilaura123",
            gender="Female",
            image="user-female.png",
            skin_test_result_id=1,
        ),
        User(
            username="Ten Ten TENNNN",
            email="tententennnnnn@example.com",
            password="tennie123",
            gender="Female",
            image="user-female.png",
            skin_test_result_id=2,
        ),
        User(
            username="faith is Fatih",
            email="faith@binus.ac.id",
            password="fatih123",
            gender="Male",
            image="user-male.png",
            skin_test_result_id=4,
        ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("✅ Users seeded successfully.")
