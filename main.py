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

    spark.sql('SELECT current_date').show()

    data = data_list

    results = spark.sparkContext.parallelize(data) \
        .map(target_function) \
        .collect()

    print(results)

    spark.stop()


if __name__ == '__main__':
    main()
