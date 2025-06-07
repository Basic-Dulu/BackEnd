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
            description="Kulit menghasilkan sebum berlebih, mudah berjerawat, dan terlihat mengilap. Pilih produk non-komedogenik dan hindari skincare yang terlalu berat.",
            characteristics="Wajah sering terlihat mengilap, terutama di area T-zone (dahi, hidung, dagu); Pori-pori besar dan terlihat jelas; Rentan terhadap jerawat, komedo, dan whiteheads; Produksi sebum (minyak alami) berlebih",
            dos="Pastikan Gizimu Seimbang: Konsumsi makanan yang kaya akan buah, sayur, serta protein tanpa lemak karena nutrisi yang baik itu penting untuk kulit yang sehat.",
            donts="Jangan Skip Pelembap: Biarpun kulitmu berminyak, nggak pakai pelembap bisa bikin kulitmu dehidrasi dan memperparah masalah tekstur kulitmu.",
        ),
        SkinTestResult(
            min_score=13,
            max_score=16,
            name="Kulit Kombinasi",
            description="Area T-zone berminyak sedangkan bagian lain (seperti pipi) bisa normal atau kering. Gunakan produk yang bisa menyeimbangkan kelembapan tanpa menyumbat pori.",
            characteristics="Kulit tampak berminyak di area T-zone, namun kering atau normal di pipi; Pori-pori besar di T-zone; Kadang timbul jerawat di area tertentu; Sulit menemukan skincare yang cocok untuk seluruh wajah",
            dos="Gunakan Skincare yang Seimbang: Pilih produk ringan yang dapat melembapkan bagian kering dan mengontrol minyak di T-zone.",
            donts="Jangan Gunakan Produk Terlalu Berat: Hindari krim yang terlalu kaya atau berminyak yang bisa menyumbat pori di area T-zone.",
        ),
        SkinTestResult(
            min_score=9,
            max_score=12,
            name="Kulit Kering",
            description="Kulit mudah terasa kaku, bersisik, dan cenderung kurang elastis. Fokus pada produk yang menghidrasi dan melembapkan kulit secara mendalam.",
            characteristics="Kulit terasa kaku dan kering setelah mencuci muka; Permukaan kulit kasar atau bersisik; Pori-pori kecil dan hampir tak terlihat; Kulit mudah iritasi atau kemerahan",
            dos="Gunakan Pelembap Secara Rutin: Pilih pelembap dengan kandungan hyaluronic acid atau ceramide untuk hidrasi ekstra.",
            donts="Hindari Sabun Wajah Keras: Jangan pakai produk pembersih yang mengandung alkohol atau terlalu banyak busa karena bisa menghilangkan kelembapan alami kulit.",
        ),
        SkinTestResult(
            min_score=5,
            max_score=8,
            name="Kulit Normal",
            description="Kulit seimbang dan tidak terlalu bermasalah. Tetap jaga dengan skincare ringan dan rutin.",
            characteristics="Kulit terasa nyaman dan tidak berminyak berlebih atau terlalu kering; Pori-pori tidak terlalu mencolok; Jarang mengalami jerawat; Warna kulit merata dan tampak segar",
            dos="Pertahankan Rutinitas Ringan: Gunakan pembersih yang lembut, pelembap ringan, dan sunscreen setiap hari.",
            donts="Jangan Gonta-Ganti Produk: Hindari mencoba terlalu banyak produk baru sekaligus agar keseimbangan kulit tidak terganggu.",
        ),
    ]

    db.session.add_all(skin_test_results)
    db.session.commit()
    print("✅ Skin Test Results seeded successfully.")
