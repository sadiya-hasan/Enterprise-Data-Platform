from src.config import (
    ORDERS_FILE,
    PROCESSED_ORDERS_PATH,
)

from src.spark_session import create_spark_session
from src.reader import read_csv
from src.loader import write_csv

spark = create_spark_session()

orders_df = read_csv(
    spark,
    ORDERS_FILE
)

write_csv(
    orders_df,
    PROCESSED_ORDERS_PATH
)

print("Orders dataset written successfully!")

spark.stop()