from src.config import ORDERS_FILE
from src.reader import read_csv
from src.spark_session import create_spark_session
from src.transformer import remove_duplicates

spark = create_spark_session()

orders_df = read_csv(spark, ORDERS_FILE)

print("Rows Before :", orders_df.count())

orders_df = remove_duplicates(orders_df)

print("Rows After  :", orders_df.count())

spark.stop()