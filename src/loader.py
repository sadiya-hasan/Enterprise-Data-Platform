"""
Loader Module
-------------
Reusable functions for writing Spark DataFrames.
"""

from pyspark.sql import DataFrame


def write_csv(
    df: DataFrame,
    output_path,
    mode: str = "overwrite"
) -> None:
    """
    Write DataFrame to CSV.
    """

    (
        df.write
        .mode(mode)
        .option("header", True)
        .csv(str(output_path))
    )