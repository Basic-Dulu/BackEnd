from app.extensions import db
from app.models.product import Product


def seed_products():
    if Product.query.first():
        print("✅ Products already seeded. Skipping.")
        return

    products = [
        Product(
            name="Low pH Gentle Jelly Cleanser",
            suitable_for="Kulit Sensitif, Kulit Kering, Kulit Berjerawat, Kulit Kemerahan",
            key_ingredient="Madecassoside, Tocopherol, Glycerin, Ceramind NP, Panthenol, Madecassoside, Aloe Barbadensis Leaf Extract, Allantoin, Dipotassium Glycyrrhizate",
            benefit="Menenangkan kemerahan & iritasi ringan, Memproteksi & memperkuat skin barrier, Mengunci kelembapan tanpa menutup pori-pori, Menjaga elastisitas kulit & mencegah tanda penuaan dini",
            product_category_id=3,
            brand_id=1,
            product_type_detail_id=1,
            ingredient_id=1,
            skin_problem_id=1,
        ),
        Product(
            name="Calm Down! Skinpair R-Cover Cream",
            suitable_for="Kulit Sensitif, Kulit Kering, Kulit Berjerawat, Kulit Kemerahan",
            key_ingredient="Madecassoside, Tocopherol, Glycerin, Ceramind NP, Panthenol, Aloe Barbadensis Leaf Extract, Allantoin, Dipotassium Glycyrrhizate",
            benefit="Menenangkan kemerahan & iritasi ringan, Memproteksi & memperkuat skin barrier, Mengunci kelembapan tanpa menutup pori-pori, Menjaga elastisitas kulit & mencegah tanda penuaan dini",
            product_category_id=2,
            brand_id=1,
            product_type_detail_id=2,
            ingredient_id=1,
            skin_problem_id=1,
        ),
        Product(
            name="Triple Care Sunscreen SPF 40 PA+++",
            suitable_for="Kulit Sensitif, Kulit Kering, Kulit Berjerawat, Kulit Kemerahan",
            key_ingredient="Madecassoside, Tocopherol, Glycerin, Ceramind NP, Panthenol, Madecassoside, Aloe Barbadensis Leaf Extract, Allantoin, Dipotassium Glycyrrhizate",
            benefit="Menenangkan kemerahan & iritasi ringan, Memproteksi & memperkuat skin barrier, Mengunci kelembapan tanpa menutup pori-pori, Menjaga elastisitas kulit & mencegah tanda penuaan dini",
            product_category_id=1,
            brand_id=3,
            product_type_detail_id=3,
            ingredient_id=1,
            skin_problem_id=3,
        ),
    ]

    db.session.add_all(products)
    db.session.commit()
    print("✅ Products seeded successfully.")
