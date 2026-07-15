"""
Reader Module
-------------
Reusable functions for reading datasets.
"""

from pyspark.sql import DataFrame


def read_csv(spark, file_path, header=True, infer_schema=True) -> DataFrame:
    return (
        spark.read
        .option("header", header)
        .option("inferSchema", infer_schema)
        .csv(str(file_path))
    )