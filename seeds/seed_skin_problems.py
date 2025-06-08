from app.extensions import db
from app.models.skin_problems import SkinProblem


def seed_skin_problems():
    if SkinProblem.query.first():
        print("✅ Skin Problems already seeded. Skipping.")
        return

    skin_problems = [
        # first question
        SkinProblem(
            name="Berjerawat",
            saw_point=0.6,
        ),
        SkinProblem(
            name="Iritasi",
            saw_point=0.3,
        ),
        SkinProblem(
            name="Kusam",
            saw_point=0.1,
        ),
    ]

    db.session.add_all(skin_problems)
    db.session.commit()
    print("✅ Skin Problems seeded successfully.")
