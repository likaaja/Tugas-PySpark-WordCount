kalimat = [
    "Apache Spark digunakan untuk memproses data dalam jumlah besar",
    "PySpark memungkinkan Python digunakan untuk menjalankan Apache Spark",
    "Pemrosesan data dapat dilakukan secara paralel menggunakan Spark",
    "Data dapat dibagi menjadi beberapa partition untuk diproses",
    "Spark memiliki konsep job stage dan task dalam pemrosesan data",
    "WordCount digunakan untuk menghitung frekuensi setiap kata",
    "Big Data membutuhkan teknik pemrosesan yang efisien",
    "Partition membantu membagi pekerjaan menjadi beberapa bagian",
    "Transformation digunakan untuk mengolah data",
    "Action digunakan untuk menjalankan proses Spark"
]

with open("data/data.txt", "w", encoding="utf-8") as file:
    for i in range(5000):
        file.write(kalimat[i % len(kalimat)] + "\n")

print("Dataset berhasil dibuat: 5000 baris")