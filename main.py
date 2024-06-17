import findspark

findspark.init()

from pyspark.sql import SparkSession
import time

possible_characters = "abcdefghijklmnopqrstuvwxyz"
base = len(possible_characters)
max_length = 5
data_list = range(0, len(possible_characters) ** max_length)
target_password = "passw"


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


def target_function(index):
    result = ''

    while index > 0 and len(result) < max_length:
        remainder = index % base
        result = possible_characters[remainder] + result
        index = index // base

    if result == target_password:
        return result

    return None


if __name__ == '__main__':
    main()
