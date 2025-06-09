from app.extensions import db
from app.models.ingredient import Ingredient


def seed_ingredients():
    if Ingredient.query.first():
        print("✅ Ingredients already seeded. Skipping.")
        return

    ingredients = [
        # 1
        Ingredient(
            name="AHA (Alpha Hydroxy Acid)",
            description="AHA adalah sekelompok asam yang bekerja dengan melonggarkan lapisan atas sel-sel kulit tua dengan memecah zat perekat yang membuat sel-sel kulit saling menyatu. Hal ini mendorong kulit untuk menumbuhkan lebih banyak sel sehingga meningkatkan pergantian sel. Ada beberapa jenis AHA yang paling terkenal yaitu lactic acid, glycolic acid, dan mandelic acid.",
            benefit="Eksfoliator kulit yang lembut, Meningkatkan tekstur kulit, Mengurangi tanda-tanda penuaan yang terlihat, Mengurangi hiperpigmentasi, Mengurangi kerusakan akibat sinar matahari, Mengurangi jerawat",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 2
        Ingredient(
            name="Allantoin",
            description="Allantoin berperan dalam menenangkan dan melembabkan kulit. Karena itu, sering ditambahkan ke produk dengan bahan aktif yang kuat. Beberapa penelitian menunjukkan bahwa bahan ini dapat mempercepat penyembuhan luka dengan konsentrasi yang lebih tinggi.",
            benefit="Melembabkan Kulit, Mengurangi Kemerahan, Mengurangi Iritasi, Baik untuk Penyembuhan Bekas Lukat",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 3
        Ingredient(
            name="Aloe Vera",
            description="Aloe Vera adalah salah satu bahan alami yang paling terkenal sebagai penenang. Kandungan ini mengandung banyak air dan memiliki efek mendinginkan dan menenangkan pada kulit, terutama saat kulit terbakar, gatal, atau iritasi. Lidah buaya juga membantu kulit untuk tetap terhidrasi serta mengandung vitamin dan nutrisi yang mendukung pemulihan kulit.",
            benefit="Melembabkan Kulit, Mengurangi Kemerahan, Mengurangi Iritasi",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=2,  # Kulit Kombinasi
        ),
        # 4
        Ingredient(
            name="Alpha Arbutin",
            description="Alpha-Arbutin merupakan antioksidan, yang berarti membantu melindungi sel-sel kulit dari kerusakan. Studi menunjukkan bahan ini membantu memperbaiki hiperpigmentasi dan memudarkan perubahan warna. Alpha-Arbutin dapat digunakan dengan bahan-bahan lain yang membantu mengatasi hiperpigmentasi seperti vitamin c, niacinamide, dan tranexamic acid.",
            benefit="Sebagai Antioksidan, Membantu Mengatasi Flek Hitam, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 5
        Ingredient(
            name="Bakuchiol",
            description=" Bakuchiol adalah antioksidan yang berasal dari tumbuhan dan sering disebut sebagai pengganti retinol meskipun bukan bagian dari keluarga yang sama. Kandungan ini memiliki efek yang sama dengan retinol dan tidak menyebabkan iritasi sebanyak retinoid tradisional. Bakuchiol bekerja dengan cara memecah radikal bebas dan merangsang produksi kolagen di kulit.",
            benefit="Sebagai Antioksidan, Mengurangi Kemerahan, Mencerahkan Kulit, Mengurangi Iritasi, Membantu Anti Penuaan, Membantu Mengatasi Flek Hitam",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 6
        Ingredient(
            name="BHA (Beta Hydroxy Acid)",
            description="Salicylic Acid (juga dikenal sebagai beta hydroxy acid atau BHA) membantu mengelupaskan permukaan dan pori-pori kulit, serta bertindak sebagai agen anti-inflamasi. Sifat multitasking ini membuatnya menjadi bahan yang bagus untuk membersihkan pori-pori, mengontrol produksi minyak, dan mengurangi peradangan. Salicylic Acid larut dalam minyak, yang berarti ia dapat mengelupas bagian dalam pori-pori dan mengurangi komedo.",
            benefit="Melawan Jerawat, Baik untuk Kulit Berminyak, Mencerahkan, Mengecilkan Pori-pori Besar",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=4,  # Kulit Normal
        ),
        # 7
        Ingredient(
            name="Centella Asiatica",
            description="Ekstrak Centella Asiatica (Centella) terkenal dengan sifat anti-inflamasi dan menenangkan, kandungan ini kaya akan antioksidan dan asam amino. Studi menunjukkan senyawa dalam centella membantu dalam mendorong kulit untuk secara alami memproduksi hyaluronic acid.",
            benefit="Mengurangi Kemerahan,  Mengurangi Iritasi, Membantu Anti Penuaan",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 8
        Ingredient(
            name="Ceramide",
            description="Ceramide merupakan bahan penyusun penting untuk pelindung kulit. Penghalang yang lebih kuat membantu kulit terlihat lebih kencang dan terhidrasi. Dengan memperkuat kulit, ceramide bertindak sebagai penghalang terhadap bahan-bahan yang mengiritasi. Kandungna ini dikenal karena kemampuannya untuk menahan air dan karenanya merupakan bahan yang bagus untuk kulit kering.",
            benefit="Melembabkan Kulit, Mengurangi Iritasi, Membantu Anti Penuaan",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 9
        Ingredient(
            name="Glycerin",
            description="Glycerin membantu melembabkan dan melindungi kulit. Sebuah studi menemukan bahwa glycerin lebih efektif sebagai humektan daripada AHA dan hyaluronic acid. Sebagai humektan, produk ini membantu kulit tetap terhidrasi dengan menarik kelembapan ke kulit. Kulit yang terhidrasi meningkatkan penghalang kulit untuk membantu melindungi kulit dari iritasi dan bakteri.",
            benefit="Melembabkan,  Mencerahkan, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 10
        Ingredient(
            name="Hyaluronic Acid",
            description="Hyaluronic Acid merupakan humektan, yaitu zat yang menarik kelembapan dari udara atau lapisan kulit yang lebih dalam dan menahannya di tempatnya untuk membantu menghidrasi dan melembutkan kulit. Kandungan ini memiliki kapasitas untuk mengikat atau menahan air dalam jumlah besar dan memiliki sifat anti-inflamasi dan anti-mikroba sehingga dapat membantu mempercepat penyembuhan luka.",
            benefit="Menghidrasi Kulit, Menenangkan Kulit, Melindungi Kulit, Membantu Anti-Penuaan, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 11
        Ingredient(
            name="Mugwort",
            description="Mugwort dikenal juga dengan ekstrak artemisia vulgaris, ekstrak ini memiliki sifat antioksidan yang kuat dan membantu meredakan iritasi. Antioksidan melindungi kulit dari kerusakan dan tanda-tanda penuaan.",
            benefit="Mengurangi Kemerahan, Mengurangi Iritasi",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 12
        Ingredient(
            name="Niacinamide",
            description="Niacinamide adalah bentuk multitasking dari vitamin B3 yang memperkuat pelindung kulit, kandungan ini lembut dan dapat ditoleransi dengan baik oleh sebagian besar jenis kulit, termasuk kulit sensitif dan reaktif. Biasanya, 5% niacinamide memberikan manfaat seperti memudarkan flek hitam. Namun, jika Anda memiliki kulit sensitif, lebih baik memulai dengan konsentrasi yang lebih kecil.",
            benefit="Menenangkan Kemerahan, Mencerahkan, Mengurangi Iritasi, Mengatur Produksi Minyak, Membantu Mengatasi Flek Hitam",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 13
        Ingredient(
            name="Oat",
            description="Oat berasal dari oatmeal koloidal,  pati dalam oatmeal koloid mampu mengikat air sehingga menjaga kulit tetap terhidrasi. Selulosa dan serat dalam oatmeal koloid membantu mengurangi peradangan sehingga dapat membantu kulit terasa lebih lembut. Oatmeal koloid juga merupakan antioksidan untuk melindungi kulit kita dari kerusakan akibat radikal bebas.",
            benefit="Sebagai Antioksidan, Melembabkan Kulit, Mengurangi kemerahan, Mengurangi iritasi",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 14
        Ingredient(
            name="Panthenol",
            description="Panthenol juga disebut sebagai pro-vitamin B, merupakan bahan umum yang membantu menghidrasi dan menenangkan kulit. Panthenol terkenal karena kemampuannya untuk masuk lebih dalam ke lapisan kulit. Seperti hyaluronic acid, panthenol adalah humektan, yaitu zat mampu mengikat dan menahan air dalam jumlah besar untuk menjaga kulit tetap terhidrasi.",
            benefit="Melembabkan, Mengurangi Kemerahan, Mengurangi Iritasi, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 15
        Ingredient(
            name="Peptide",
            description="Peptide adalah rantai pendek asam amino yang membentuk protein tertentu yang dibutuhkan oleh kulit. Peptide dapat menembus lapisan luar kulit, jadi alih-alih berada di atas kulit, peptide akan meresap lebih dalam. Kandungan ini dapat dianggap sebagai pembawa pesan untuk sel-sel lain. Mereka mengirimkan sinyal yang memberi tahu sel-sel untuk memproduksi kolagen dan elastin.",
            benefit="Memperbaiki lapisan kulit, Mengurangi kerutan, Kulit lebih elastis, Meredakan peradangan, Membantu menghilangkan jerawat",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 16
        Ingredient(
            name="PHA (Polyhydroxy Acid)",
            description="PHA bekerja dengan mengelupaskan sel-sel kulit mati di permukaan, menghasilkan warna dan tekstur kulit yang lebih merata, dan juga membantu bahan-bahan perawatan kulit menembus lebih dalam ke lapisan kulit sehingga dapat meningkatkan khasiatnya. Kandungan ini juga kaya akan antioksidan dan merangsang pertumbuhan dan perbaikan epidermis, yaitu lapisan terluar dari kulit yang berfungsi sebagai pelindung.",
            benefit="Eksfoliator kulit yang lembut, Menghidrasi Kulit, Anti-penuaan, Anti-inflamasi, Memperbaiki kerusakan akibat sinar matahari",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 17
        Ingredient(
            name="Propolis",
            description="Ekstrak Propolis memiliki sifat antimikroba, anti-inflamasi, penyembuhan luka, dan antioksidan. Penelitian menunjukkan propolis membantu melawan bakteri, virus, dan jamur sehingga dapat membantu mengurangi jerawat dan mempercepat penyembuhan luka. Sebuah studi menemukan bahwa propolis dapat membantu membalikkan kerusakan kulit akibat sinar UV.",
            benefit="Melawan Jerawat, Mengurangi Kemerahan, Mengurangi Iritasi, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 18
        Ingredient(
            name="Squalane",
            description="Squalane membantu kulit mempertahankan kelembapan dan merupakan emolien, yaitu bahan yang membentuk lapisan pelindung tipis pada kulit untuk menahan kelembapan dan membantu meredakan kulit kering, gatal, atau bersisik. Squalane berasal dari squalene, yang diproduksi secara alami di dalam sebum kulit kita untuk menjaga kulit tetap terhidrasi.",
            benefit="Menghidrasi Kulit, Membantu melawan radikal bebas, Membantu melawan kerusakan kulit",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 19
        Ingredient(
            name="Tranexamic Acid",
            description=" Tranexamic Acid paling baik digunakan untuk mengobati hiperpigmentasi, perubahan warna, dan melasma. Kandungan ini juga dapat membantu membangun pelindung kulit yang lebih kuat, mencegah sel-sel kulit kita bertemu dengan sel-sel produksi pigmen, dan mengurangi peradangan akibat paparan sinar UV. Sifatnya yang mencerahkan membuatnya sangat baik dalam mengurangi munculnya bekas jerawat dan bekas luka.",
            benefit="Mengurangi Iritasi, Membantu mengatasi Flek Hitam, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=1,  # Lembut
            skin_test_result_id=1,  # Kulit Berminyak
        ),
        # 20
        Ingredient(
            name="Vitamin C",
            description="Vitamin C paling baik digunakan untuk mencerahkan kulit. Kandungan ini dapat memperbaiki bintik-bintik hitam, bekas jerawat, dan hiperpigmentasi karena vitamin C menghalangi proses penggelapan kulit saat terpapar sinar UV.",
            benefit="Sebagai Antioksidan, Mengurangi Kemerahan, Mencerahkan, Baik untuk Tekstur Kulit, Mengecilkan Pori-pori Besar, Membantu Anti Penuaan, Baik untuk Penyembuhan Bekas Luka",
            ingredient_type_id=2,  # Keras
            skin_test_result_id=1,  # Kulit Berminyak
        ),
    ]

    db.session.add_all(ingredients)
    db.session.commit()
    print("✅ Ingredients seeded successfully.")
