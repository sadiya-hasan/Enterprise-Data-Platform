from src.spark_session import create_spark_session

spark = create_spark_session()

print("Spark Version:", spark.version)

spark.stop()