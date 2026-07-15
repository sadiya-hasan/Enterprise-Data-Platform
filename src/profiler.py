"""
Profiler Module
---------------
Reusable functions for profiling Spark DataFrames.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count, when


def print_schema(df: DataFrame) -> None:
    """
    Print DataFrame schema.
    """
    print("\nSchema:")
    df.printSchema()


def show_sample_data(
    df: DataFrame,
    rows: int = 10,
    truncate: bool = False
) -> None:
    """
    Display sample records.
    """
    print(f"\nFirst {rows} Records:")
    df.show(rows, truncate=truncate)


def dataset_summary(df: DataFrame) -> None:
    """
    Display dataset summary.
    """
    total_records = df.count()
    total_columns = len(df.columns)

    print("\nDataset Summary")
    print("----------------")
    print(f"Total Records : {total_records}")
    print(f"Total Columns : {total_columns}")


def null_value_summary(df: DataFrame) -> None:
    """
    Display NULL count for every column.
    """
    print("\nNULL Values")

    null_df = df.select(
        [
            count(when(col(column).isNull(), column)).alias(column)
            for column in df.columns
        ]
    )

    null_df.show(truncate=False)


def duplicate_summary(
    df: DataFrame,
    primary_key: str
) -> None:
    """
    Display duplicate count for primary key.
    """

    duplicate_count = (
        df.groupBy(primary_key)
        .count()
        .filter(col("count") > 1)
        .count()
    )

    print(f"\nDuplicate {primary_key}: {duplicate_count}")


def distinct_values(
    df: DataFrame,
    column_name: str
) -> None:
    """
    Display distinct values of a column.
    """

    print(f"\nDistinct Values of '{column_name}'")

    df.select(column_name).distinct().show(truncate=False)