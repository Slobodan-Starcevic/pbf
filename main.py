from pyspark.sql import SparkSession
import os

from target_file import target_function
from target_file import data_list
from util import get_spark_session


def main():
    spark = SparkSession.builder \
        .master('local[*]') \
        .appName("pbf") \
        .getOrCreate()

    rdd = spark.sparkContext.parallelize(data_list)

    result = rdd.map(target_function).filter(lambda x: x is not None).collect()

    print(result)

    spark.stop()


if __name__ == '__main__':
    main()
