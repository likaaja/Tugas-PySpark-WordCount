from pyspark.sql import SparkSession

# 1. Inisialisasi Spark
spark = SparkSession.builder \
    .appName("WordCount PySpark") \
    .getOrCreate()

# 2. Membaca data
text = spark.sparkContext.textFile("data/data.txt")

# 3. WordCount
words = text.flatMap(lambda line: line.lower().split())

word_counts = words.map(lambda word: (word, 1)) \
                   .reduceByKey(lambda a, b: a + b)

# 4. Mengurutkan dari jumlah terbanyak
top_10 = word_counts.sortBy(
    lambda x: x[1],
    ascending=False
).take(10)

# 5. Menampilkan 10 kata terbanyak
print("\n=== 10 KATA TERBANYAK ===")

for word, count in top_10:
    print(f"{word}: {count}")

# 6. Menampilkan jumlah partition
print("\nJumlah partition:", word_counts.getNumPartitions())

input("Tekan ENTER untuk menutup Spark...")
spark.stop()