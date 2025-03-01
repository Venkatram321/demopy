from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Example with Python 3.8") \
    .getOrCreate()

data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

df.show()
print("Venkat")

print("Hyderabad")
spark.stop()
