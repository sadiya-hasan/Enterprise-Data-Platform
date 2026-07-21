"""
Transformer Module
------------------
Reusable transformation functions for Spark DataFrames.
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col


def remove_duplicates(df: DataFrame) -> DataFrame:
    """
    Remove completely duplicate rows.
    """
    return df.dropDuplicates()


def remove_duplicates_by_column(
    df: DataFrame,
    column_name: str
) -> DataFrame:
    """
    Remove duplicate rows based on a specific column.
    """
    return df.dropDuplicates([column_name])


def drop_columns(
    df: DataFrame,
    columns: list
) -> DataFrame:
    """
    Drop one or more columns.
    """
    return df.drop(*columns)


def rename_column(
    df: DataFrame,
    old_name: str,
    new_name: str
) -> DataFrame:
    """
    Rename a column.
    """
    return df.withColumnRenamed(old_name, new_name)


def fill_null_values(
    df: DataFrame,
    value
) -> DataFrame:
    """
    Replace NULL values with a given value.
    """
    return df.fillna(value)


def drop_null_rows(df: DataFrame) -> DataFrame:
    """
    Remove rows containing NULL values.
    """
    return df.dropna()


def cast_column(
    df: DataFrame,
    column_name: str,
    data_type: str
) -> DataFrame:
    """
    Cast a column to another datatype.
    """
    return df.withColumn(
        column_name,
        col(column_name).cast(data_type)
    )