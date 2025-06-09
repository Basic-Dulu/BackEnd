from app.extensions import db
from app.models.skincare_category import SkinCareCategory


def seed_skincare_categories():
    if SkinCareCategory.query.first():
        print("✅ Skincare Categories already seeded. Skipping.")
        return

    skincare_categories = [
        SkinCareCategory(
            name="First Cleanser",
            slogan="Double Cleanse, Double Fresh!",
            description="First cleanser adalah tahap awal pembersihan wajah yang biasanya berbahan dasar minyak atau balm. Produk ini membantu melarutkan makeup, sunscreen, dan kotoran berbasis minyak.",
            image="first-cleanser.png",
            benefit="Membersihkan makeup dan sunscreen, Mengangkat kotoran berbasis minyak, Menjaga kelembaban kulit saat membersihkan, Persiapan optimal untuk pembersih kedua",
            how_to_use="Gunakan pada wajah yang kering., Pijat dengan lembut selama 1-2 menit untuk melarutkan makeup dan kotoran., Bilas dengan air hangat atau lap dengan handuk basah., Lanjutkan dengan second cleanser (face wash).",
        ),
        SkinCareCategory(
            name="Face Wash",
            slogan="Cleansing that cares!",
            description="Face wash atau second cleanser digunakan setelah first cleanser untuk membersihkan sisa kotoran, minyak, dan residu dari kulit. Biasanya berbasis air dan menghasilkan busa.",
            image="face-wash.png",
            benefit="Membersihkan sisa kotoran dan minyak, Menyegarkan kulit wajah, Membantu mencegah jerawat, Menyeimbangkan pH kulit",
            how_to_use="Basahi wajah dengan air., Ambil secukupnya dan busakan di tangan., Usapkan ke wajah dengan gerakan memijat., Bilas hingga bersih dan keringkan dengan handuk bersih.",
        ),
        SkinCareCategory(
            name="Moisturizer",
            slogan="Keeps your skin hydrated!",
            description="Moisturizer atau pelembab adalah produk perawatan kulit yang menghidrasi kulit dengan menyerap air. Pelembap membantu menjaga fungsi lapisan kulit, memperbaiki tekstur, dan melindungi dari kerusakan lingkungan",
            image="moisturizer.png",
            benefit="Melembabkan kulit, Melindungi lapisan kulit, Memperbaiki tekstur kulit, Mempersiapkan kulit untuk tabir surya",
            how_to_use="Bersihkan wajah secara menyeluruh dan keringkan dengan menepuk-nepuknya., Ambil pelembab seukuran kacang polong., Oleskan secara merata ke seluruh wajah dan leher dengan lembut., Gunakan dua kali sehari — di pagi hari dan sebelum tidur.",
        ),
        SkinCareCategory(
            name="SPF",
            slogan="Your daily skin shield!",
            description="SPF (Sun Protection Factor) adalah produk yang melindungi kulit dari paparan sinar UV berbahaya. Penggunaan SPF secara rutin membantu mencegah penuaan dini dan kanker kulit.",
            image="spf.png",
            benefit="Melindungi kulit dari sinar UVA dan UVB, Mencegah penuaan dini, Mengurangi risiko kanker kulit, Menjaga warna kulit tetap merata",
            how_to_use="Gunakan sebagai langkah terakhir di pagi hari., Aplikasikan 15 menit sebelum terpapar matahari., Gunakan secukupnya dan ratakan ke seluruh wajah dan leher., Reaplikasikan setiap 2 jam bila terpapar sinar matahari secara langsung.",
        ),
    ]

    db.session.add_all(skincare_categories)
    db.session.commit()
    print("✅ Skincare Categories seeded successfully.")
