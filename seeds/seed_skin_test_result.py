from app.extensions import db
from app.models.skin_test_result import SkinTestResult


def seed_skin_test_results():
    if SkinTestResult.query.first():
        print("✅ Skin Test Results already seeded. Skipping.")
        return

    skin_test_results = [
        SkinTestResult(
            min_score=17,
            max_score=20,
            name="Kulit Berminyak",
            description="Kulit berminyak tampak halus dan mengilap akibat produksi minyak berlebih pada kulit. Faktor yang memengaruhi kulit berminyak adalah genetika, perubahan hormon, dan stres.",
            characteristics="Terlihat mengkilap terutama di daerah T-zone (dahi, hidung, dan dagu); Pori-pori besar dan nampak jelas; Rentan terhadap keluhan jerawat atau komedo; Produksi sebum (minyak alami) berlebih",
            dos="Perhatikan keterangan produk skincare, gunakan produk perawatan kulit dengan keterangan non-comedogenic sehingga tidak menyebabkan sumbatan.",
            donts="Jangan lupa pakai pelembap, namun hindari produk yang mengandung komponen atau pelembab krim yang berat.",
            saw_point=0.4,
        ),
        SkinTestResult(
            min_score=13,
            max_score=16,
            name="Kulit Kombinasi",
            description="Kulit kombinasi merupakan gabungan antara kulit berminyak dan kering. Jenis kulit kombinasi dipengaruhi oleh perkembangan pubertas dan hormon. Untuk itu, perawatan kulit kombinasi harus mampu mengurangi kadar minyak di bagian T tetapi juga melembabkan pipi.",
            characteristics="Berminyak di bagian T-zone (dahi, hidung, dagu); Bagian pipi cenderung kering atau normal; Perubahan kondisi kulit sesuai cuaca; Pori-pori lebih besar di area T-zone",
            dos="Sesuaikan perawatan dengan area kulit, area kering dapat menggunakan pelembab lebih banyak, sementara area berminyak menggunakan produk yang menyerap minyak berlebih.",
            donts="Jangan pakai produk yang terlalu keras, hindari pembersih yang terlalu keras yang bisa memperparah ketidakseimbangan kulit.",
            saw_point=0.3,
        ),
        SkinTestResult(
            min_score=9,
            max_score=12,
            name="Kulit Kering",
            description="Kulit kering umumnya tampak kasar dan terkadang mengelupas halus akibat rendahnya kadar air pada kulit. Keluhan pada jenis kulit kering pada umumnya adalah kulit tampak kusam. Hal tersebut dapat dipengaruhi oleh perubahan hormon, efek samping obat-obatan, paparan sinar matahari, dan pengaruh cuaca dingin.",
            characteristics="Memiliki pori-pori kecil yang bahkan tidak terlihat; Tekstur kulit cenderung kasar dan bersisik; Terasa dehidrasi dan mungkin menyebabkan rasa gatal atau iritasi; Kurang elastis dan garis-garis lebih terlihat",
            dos="Selalu pakai pelembap, gunakan pelembap setiap hari pada wajah, leher, dan juga kulit di sekitar mata sebagai antisipasi untuk mencegah timbulnya keriput dini.",
            donts="Jangan cuci muka dengan air panas, hindari penggunaan produk pembersih yang terlalu keras serta mencuci muka dengan air yang terlalu panas karena dapat menghilangkan minyak alami kulit.",
            saw_point=0.2,
        ),
        SkinTestResult(
            min_score=5,
            max_score=8,
            name="Kulit Normal",
            description="Kandungan air dan minyak pada kulit seimbang sehingga kulit tampak halus, kenyal, tidak terlalu kering atau terlalu berminyak. Biasanya jenis kulit normal memiliki keluhan wajah yang minim dan mudah dirawat dibandingkan dengan jenis kulit lainnya.",
            characteristics="Memiliki pori-pori yang kecil; Tekstur kulit halus; Tidak terasa terlalu kering atau berminyak; Cenderung terbebas dari masalah jerawat",
            dos="Tetap jaga keseimbangan kulit, gunakan produk ringan untuk mempertahankan kondisi kulit yang baik.",
            donts="Jangan lupa pakai sunscreen, meskipun kulit normal — sunscreen tetap wajib dipakai setiap hari untuk menghindari kerusakan kulit akibat sinar UV.",
            saw_point=0.1,
        ),
    ]

    db.session.add_all(skin_test_results)
    db.session.commit()
    print("✅ Skin Test Results seeded successfully.")
