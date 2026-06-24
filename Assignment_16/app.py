from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Assignment16").getOrCreate()

sc = spark.sparkContext

rdd = sc.textFile("employee_data.csv")

header = rdd.first()

employees = rdd.filter(lambda x: x != header).map(
    lambda x: (
        int(x.split(",")[0]),
        x.split(",")[1],
        x.split(",")[2],
        int(x.split(",")[3])
    )
)

print("Employees Sorted by Salary")

sorted_employees = employees.sortBy(lambda x: x[3], ascending=False)

for emp in sorted_employees.collect():
    print(emp)

print("\nDepartment Wise Salary Total")

dept_salary = employees.map(
    lambda x: (x[2], x[3])
).reduceByKey(
    lambda a, b: a + b
)

for item in dept_salary.collect():
    print(item)

print("\nTop 3 Highest Paid Employees")

top3 = sorted_employees.take(3)

for emp in top3:
    print(emp)

sc.parallelize(
    [str(emp) for emp in top3]
).saveAsTextFile("output/top3_employees")

spark.stop()