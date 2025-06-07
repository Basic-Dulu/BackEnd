from app.extensions import db
from app.models.skin_test_question import SkinTestQuestion


def seed_skin_test_questions():
    if SkinTestQuestion.query.first():
        print("✅ Skin Test Questions already seeded. Skipping.")
        return

    skin_test_questions = [
        SkinTestQuestion(
            question="Bagaimana kondisi kulit wajahmu saat bangun tidur (tanpa menggunakan skincare malam)?",
        ),
        SkinTestQuestion(
            question="Setelah mencuci muka dengan sabun wajah, apa yang kamu rasakan?",
        ),
        SkinTestQuestion(
            question="Bagaimana pori-pori kulit wajahmu?",
        ),
        SkinTestQuestion(
            question="Apakah kamu sering mengalami jerawat atau komedo?",
        ),
        SkinTestQuestion(
            question="Bagaimana kondisi kulitmu saat berada di ruangan ber-AC dalam waktu lama?",
        ),
    ]

    db.session.add_all(skin_test_questions)
    db.session.commit()
    print("✅ Skin Test Questions seeded successfully.")
