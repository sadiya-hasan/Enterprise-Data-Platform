from src.config import ORDERS_FILE
from src.reader import read_csv
from src.spark_session import create_spark_session
from src.profiler import (
    print_schema,
    show_sample_data,
    dataset_summary,
    null_value_summary,
    duplicate_summary,
    distinct_values,
)

spark = create_spark_session()

orders_df = read_csv(spark, ORDERS_FILE)

print_schema(orders_df)

show_sample_data(orders_df)

dataset_summary(orders_df)

null_value_summary(orders_df)

duplicate_summary(
    orders_df,
    "order_id"
)

distinct_values(
    orders_df,
    "order_status"
)

spark.stop()