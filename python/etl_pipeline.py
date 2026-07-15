import os
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, when

# ==========================================================
# Configure PySpark to use the current Python interpreter
# ==========================================================
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

# ==========================================================
# Create Spark Session
# ==========================================================
spark = (
    SparkSession.builder
    .appName("Enterprise Data Platform")
    .master("local[*]")
    .getOrCreate()
)

# ==========================================================
# Read Orders Dataset
# ==========================================================
orders_df = spark.read.csv(
    "data/raw/kaggle/olist_orders_dataset.csv",
    header=True,
    inferSchema=True
)

# ==========================================================
# Dataset Overview
# ==========================================================
print("\n==================================================")
print("              ORDERS DATASET")
print("==================================================")

print("\nSchema:")
orders_df.printSchema()

print("\nFirst 10 Records:")
orders_df.show(10, truncate=False)

# Store values in variables
total_records = orders_df.count()
total_columns = len(orders_df.columns)

print(f"\nTotal Records : {total_records}")
print(f"Total Columns : {total_columns}")

# ==========================================================
# Data Profiling
# ==========================================================
print("\n==================================================")
print("              DATA PROFILING")
print("==================================================")

# Count NULL values in each column
null_df = orders_df.select(
    [
        count(when(col(column).isNull(), column)).alias(column)
        for column in orders_df.columns
    ]
)

print("\nNull Values in Each Column:")
null_df.show(truncate=False)

# Count duplicate Order IDs
duplicate_order_ids = (
    orders_df.groupBy("order_id")
    .count()
    .filter(col("count") > 1)
    .count()
)

print(f"\nDuplicate Order IDs : {duplicate_order_ids}")

# Display distinct Order Status values
print("\nDistinct Order Statuses:")
orders_df.select("order_status").distinct().show(truncate=False)

# ==========================================================
# Stop Spark Session
# ==========================================================
spark.stop()