import os
os.environ["PYTHONWARNINGS"] = "ignore"

import time
from pyspark.sql import SparkSession

# Membuat Spark
spark = SparkSession.builder \
    .appName("Uji Partition WordCount") \
    .getOrCreate()

# Mengurangi warning di terminal
spark.sparkContext.setLogLevel("ERROR")

# Membaca dataset
text = spark.sparkContext.textFile("data/data.txt")

# Percobaan jumlah partition
partition_list = [1, 2, 4, 8, 16]

print("\n=== HASIL UJI PARTITION ===")

for jumlah_partition in partition_list:

    # Membagi data menjadi beberapa partition
    data = text.repartition(jumlah_partition)

    # Mulai menghitung waktu
    start_time = time.perf_counter()

    # WordCount
    hasil = data \
        .flatMap(lambda line: line.lower().split()) \
        .map(lambda word: (word, 1)) \
        .reduceByKey(
            lambda a, b: a + b,
            numPartitions=jumlah_partition
        )

    # Action untuk menjalankan proses Spark
    hasil.count()

    # Menghitung waktu
    end_time = time.perf_counter()
    waktu = end_time - start_time

    print(
        f"Partition: {jumlah_partition} | "
        f"Waktu: {waktu:.4f} detik"
    )

spark.stop()