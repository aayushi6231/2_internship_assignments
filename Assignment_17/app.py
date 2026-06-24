from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Assignment17").getOrCreate()

df = spark.read.csv("sales_data.csv", header=True, inferSchema=True)

print("Sorted Products")

sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

print("Top 3 Products")

top3 = sorted_df.limit(3)
top3.show()

print("Sales Greater Than 80000")

high_sales = df.filter(col("sales") > 80000)
high_sales.show()

high_sales.coalesce(1).write.mode("overwrite").option("header", "true").csv("output/high_sales_products")

spark.stop()