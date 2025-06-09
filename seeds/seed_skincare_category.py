from app.extensions import db
from app.models.skincare_category import SkinCareCategory


def seed_skincare_categories():
    if SkinCareCategory.query.first():
        print("✅ Skincare Categories already seeded. Skipping.")
        return

    skincare_categories = [
        SkinCareCategory(
            name="First Cleanser",
            slogan="Double Cleanse, Double the Benefits!",
            description="First Cleanser adalah produk pembersih yang digunakan sebagai langkah awal untuk menghilangkan kotoran dari permukaan kulit. Penggunaan first cleanser sebelum sabun cuci muka disebut juga dengan metode Double Cleansing.",
            image="first-cleanser.png",
            benefit="Menghilangkan kotoran dan sisa produk waterproof, termasuk polusi, Membersihkan wajah sampai ke pori-pori, Memaksimalkan penyerapan skincare, Mencegah masalah kulit akibat pori yang tersumbat",
            how_to_use="Pastikan wajah kamu dalam kondisi kering dan ambil first cleanser secukupnya, Pijat first cleanser ke wajah, atau gunakan kapas kalau kamu menggunakan produk berbasis air, Kalau kamu menggunakan produk berbasis minyak, tambahkan sedikit air untuk mengemulsikannya, Bilas sampai bersih dengan air, pastikan semua residu sudah hilang",
        ),
        SkinCareCategory(
            name="Cleanser",
            slogan="Clear Skin Starts Here!",
            description="Sabun cuci muka adalah produk yang penting dalam rutinitas skincare, berfungsi untuk membersihkan, melindungi, dan merawat kulit wajah, serta mencegah  berbagai masalah kulit seperti jerawat.",
            image="face-wash.png",
            benefit="Membersihkan dan menghilangkan kotoran di kulit, Mencegah jerawat dengan menjaga pori-pori tetap bersih, Mempersiapkan kulit untuk produk skincare selanjutnya, Membantu menciptakan kulit yang lebih sehat",
            how_to_use="Pastikan cuci tangan terlebih dahulu untuk menghindari perpindahan kotoran atau bakteri ke wajah, Basahi wajah dan aplikasikan produk ke wajah — termasuk leher, hindari menggosok kulit dengan kasar, Bilas wajah dengan air, pastikan semua sisa sabun cuci muka sudah hilang, Tepuk-tepuk wajah hingga kering dengan handuk yang kering, bersih, dan lembut.",
        ),
        SkinCareCategory(
            name="Moisturizer",
            slogan="Keeps Your Skin Hydrated!",
            description="Moisturizer atau pelembab adalah produk perawatan kulit yang menghidrasi kulit dengan menyerap air. Pelembap membantu menjaga fungsi lapisan kulit, memperbaiki tekstur kulit, dan melindungi kulit dari kerusakan lingkungan.",
            image="moisturizer.png",
            benefit="Melembabkan kulit, Melindungi lapisan kulit, Memperbaiki tekstur kulit, Mempersiapkan kulit untuk tabir surya",
            how_to_use="Bersihkan wajah secara menyeluruh dan keringkan dengan menepuk-nepuknya, Ambil produk pelembab secukupnya untuk seluruh wajah, Oleskan secara merata ke seluruh wajah dan leher dengan lembut, Gunakan dua kali sehari — di pagi hari dan sebelum tidur",
        ),
        SkinCareCategory(
            name="Sunscreen",
            slogan="Sun Kissed Not Sunburned!",
            description="Sunscreen melindungi kulit dari efek merusak radiasi matahari, seperti penuaan dini, hiperpigmentasi, dan risiko kanker kulit. Penggunaan sunscreen secara rutin terbukti mencegah kerusakan akibat sinar UV setelah pemakaian jangka panjang.",
            image="spf.png",
            benefit="Melindungi kulit dari sinar UVB yang merupakan penyebab utama kulit terbakar, Menghalangi sinar UVA yang berkontribusi terhadap penuaan dini, Mengurangi risiko kanker kulit, Mencegah hiperpigmentasi dengan menghalangi sinar UV",
            how_to_use="Pilih sunscreen yang ditandai dengan adanya SPF dan PA, dengan minimal SPF 30, Pastikan wajah dalam keadaan bersih sebelum menggunakan sunscreen, Gunakan sunscreen dengan takaran 2 jari dan oleskan secara merata ke seluruh wajah dan leher, Tunggu 15-30 menit sebelum terpapar sinar matahari",
        ),
    ]

    db.session.add_all(skincare_categories)
    db.session.commit()
    print("✅ Skincare Categories seeded successfully.")
