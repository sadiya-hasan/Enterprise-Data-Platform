from src.config import ORDERS_FILE
from src.reader import read_csv
from src.spark_session import create_spark_session

spark = create_spark_session()

orders_df = read_csv(spark, ORDERS_FILE)

print("Rows :", orders_df.count())
print("Columns :", len(orders_df.columns))

spark.stop()