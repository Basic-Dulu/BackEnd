from app.extensions import db
from app.models.skin_test_options import SkinTestOption


def seed_skin_test_options():
    if SkinTestOption.query.first():
        print("✅ Skin Test Options already seeded. Skipping.")
        return

    skin_test_options = [
        # first question
        SkinTestOption(
            option="Terasa berminyak di seluruh wajah",
            question_id=1,
            point=4,
        ),
        SkinTestOption(
            option="Berminyak di area T-zone (dahi, hidung, dagu), kering di pipi",
            question_id=1,
            point=3,
        ),
        SkinTestOption(
            option="Kering dan terasa kaku",
            question_id=1,
            point=2,
        ),
        SkinTestOption(
            option="Tidak berminyak dan tidak kering, terasa normal",
            question_id=1,
            point=1,
        ),
        # second option
        SkinTestOption(
            option="Kulit cepat berminyak kembali",
            question_id=2,
            point=4,
        ),
        SkinTestOption(
            option="Pipi terasa kering, tapi T-zone tetap berminyak",
            question_id=2,
            point=3,
        ),
        SkinTestOption(
            option="Kulit terasa sangat kering, ketarik, bahkan bersisik",
            question_id=2,
            point=2,
        ),
        SkinTestOption(
            option="Kulit terasa segar dan nyaman",
            question_id=2,
            point=1,
        ),
        # third question
        SkinTestOption(
            option="Besar dan terlihat jelas di seluruh wajah",
            question_id=3,
            point=4,
        ),
        SkinTestOption(
            option="Besar di T-zone, kecil di pipi",
            question_id=3,
            point=3,
        ),
        SkinTestOption(
            option="Kecil dan hampir tidak terlihat",
            question_id=3,
            point=2,
        ),
        SkinTestOption(
            option="Ukuran normal dan tidak terlalu mencolok",
            question_id=3,
            point=1,
        ),
        # fourth question
        SkinTestOption(
            option="Sangat sering, terutama jerawat aktif",
            question_id=4,
            point=4,
        ),
        SkinTestOption(
            option="Kadang-kadang di area T-zone",
            question_id=4,
            point=3,
        ),
        SkinTestOption(
            option="Jarang, hampir tidak pernah",
            question_id=4,
            point=2,
        ),
        SkinTestOption(
            option="Tidak terlalu sering, hanya sesekali",
            question_id=4,
            point=1,
        ),
        # fifth question
        SkinTestOption(
            option="Tetap berminyak",
            question_id=5,
            point=4,
        ),
        SkinTestOption(
            option="T-zone sedikit berminyak, pipi terasa kering",
            question_id=5,
            point=3,
        ),
        SkinTestOption(
            option="Kulit terasa sangat kering dan gatal",
            question_id=5,
            point=2,
        ),
        SkinTestOption(
            option="Kulit tetap nyaman dan tidak terlalu berubah",
            question_id=5,
            point=1,
        ),
    ]

    db.session.add_all(skin_test_options)
    db.session.commit()
    print("✅ Skin Test Options seeded successfully.")
