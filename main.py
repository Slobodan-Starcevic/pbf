import findspark

findspark.init()

from pyspark.sql import SparkSession
from target_file import target_function
from target_file import data_list
import time


def main():
    spark = SparkSession.builder \
        .master('local[*]') \
        .appName("pbf") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    time_start = time.time()

    rdd = spark.sparkContext.parallelize(data_list)
    result = rdd.map(target_function).filter(lambda x: x is not None).collect()

    print(result, f"{(time.time() - time_start)} seconds taken")

    spark.stop()


if __name__ == '__main__':
    main()
