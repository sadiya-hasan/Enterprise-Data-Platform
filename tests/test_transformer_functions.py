from src.config import ORDERS_FILE
from src.reader import read_csv
from src.spark_session import create_spark_session
from src.transformer import rename_column

spark = create_spark_session()

orders_df = read_csv(spark, ORDERS_FILE)

print("\nOriginal Columns:")
print(orders_df.columns)

orders_df = rename_column(
    orders_df,
    "order_status",
    "status"
)

print("\nRenamed Columns:")
print(orders_df.columns)

spark.stop()