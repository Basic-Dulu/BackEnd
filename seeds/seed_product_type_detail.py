from app.extensions import db
from app.models.product_type_detail import ProductTypeDetail


def seed_product_type_details():
    if ProductTypeDetail.query.first():
        print("✅ Product Type Details already seeded. Skipping.")
        return

    product_type_details = [
        # 1. Cleansing Balm
        ProductTypeDetail(
            description="Cleansing balm sangat efektif membersihkan produk waterproof, sunscreen, dan sebum berlebih tanpa merusak lapisan pelindung kulit.",
            product_type_id=1,
            skincare_category_id=1,
        ),
        # 2. Cleansing Milk
        ProductTypeDetail(
            description="Cleansing milk juga efektif membersihkan kotoran serta membantu menjaga keseimbangan kelembapan dan pH kulit.",
            product_type_id=2,
            skincare_category_id=1,
        ),
        # 3. Cleansing Oil
        ProductTypeDetail(
            description="Cleansing oil efektif membersihkan produk tahan air tanpa menyebabkan iritasi atau polusi sekunder pada kulit.",
            product_type_id=3,
            skincare_category_id=1,
        ),
        # 4. Micellar Water
        ProductTypeDetail(
            description="Micellar water mengandung micelles yang dapat mengikat kotoran dan minyak, sehingga efektif membersihkan kulit tanpa mengiritasi.",
            product_type_id=4,
            skincare_category_id=1,
        ),
        # 5 Cream Cleanser
        ProductTypeDetail(
            description="Sabun cuci muka dengan tekstur krim yang berfungsi untuk membersihkan wajah secara lembut, cocok untuk berbagai jenis kulit, terutama kulit kering.",
            product_type_id=5,
            skincare_category_id=2,
        ),
        # 6. Gel Cleanser
        ProductTypeDetail(
            description="Cocok untuk kulit berminyak atau sensitif karena tidak mengandung minyak dan mudah dibilas tanpa meninggalkan residu berat di kulit.",
            product_type_id=6,
            skincare_category_id=2,
        ),
        # 7. Foaming Cleanser
        ProductTypeDetail(
            description="Memberikan pembersihan yang lembut namun efektif, sehingga cocok untuk semua jenis kulit, terutama kulit sensitif.",
            product_type_id=7,
            skincare_category_id=2,
        ),
        # 8. Gel Moisturizer
        ProductTypeDetail(
            description="Ringan, berbahan dasar air, cepat menyerap, dan tidak meninggalkan rasa lengket atau berminyak, sehingga cocok untuk kulit berminyak.",
            product_type_id=8,
            skincare_category_id=3,
        ),
        # 9. Cream Moisturizer
        ProductTypeDetail(
            description="Memberikan kelembapan lebih intens dan membantu memperbaiki fungsi pelindung kulit, sehingga lebih sesuai untuk kulit kering atau sensitif.",
            product_type_id=9,
            skincare_category_id=3,
        ),
        # 10. Physical Sunscreen
        ProductTypeDetail(
            description="Dikenal juga sebagai mineral sunscreen, bekerja dengan membentuk lapisan pelindung di permukaan kulit untuk memantulkan sinar UV.",
            product_type_id=10,
            skincare_category_id=4,
        ),
        # 11. Chemical Sunscreen
        ProductTypeDetail(
            description="Menyerap sinar UV dan mengubahnya menjadi energi panas yang tidak berbahaya bagi kulit.",
            product_type_id=11,
            skincare_category_id=4,
        ),
        # 12. Hybrid Sunscreen
        ProductTypeDetail(
            description="Sunscreen yang menggabungkan formula physical sunscreen dan chemical sunscreen, bertujuan untuk memberikan perlindungan lebih maksimal.",
            product_type_id=12,
            skincare_category_id=4,
        ),
    ]

    db.session.add_all(product_type_details)
    db.session.commit()
    print("✅ Product Type Details seeded successfully.")
