"""
Spark Session Module
--------------------
Creates and returns a SparkSession.
"""

import os
import sys

from pyspark.sql import SparkSession


def create_spark_session(app_name="Enterprise Data Platform"):
    """
    Create and return a SparkSession.
    """

    # Configure PySpark to use the current Python interpreter
    os.environ["PYSPARK_PYTHON"] = sys.executable
    os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .getOrCreate()
    )

    return spark