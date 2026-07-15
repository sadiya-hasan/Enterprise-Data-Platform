import os
import sys

# Tell Spark exactly which Python to use
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

print("Python executable:", sys.executable)

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("Enterprise Data Platform")
    .master("local[*]")
    .getOrCreate()
)

employees = [
    (101, "Alice", "HR", 50000),
    (102, "Bob", "IT", 75000),
    (103, "Charlie", "Finance", 68000),
    (104, "David", "IT", 82000),
]

df = spark.createDataFrame(
    employees,
    ["emp_id", "name", "department", "salary"]
)

df.show()

spark.stop()