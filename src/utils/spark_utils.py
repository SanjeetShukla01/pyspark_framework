import sys

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType

from src.utils.logging_utils import Logger


class SparkUtils:
    logger = Logger(__name__).get_logger()

    def get_spark_session(self, app_name: str) -> SparkSession:
        """
        This function creates spark session
        :param app_name:    Name of the pyspark app for SparkSession
        :return:            Returns SparkSession
        """
        try:
            spark_session = SparkSession.builder.appName(app_name).enableHiveSupport().getOrCreate()
            return spark_session
        except Exception as error_message:
            self.logger.info(" Failed to create sparkSession")
            self.logger.exception("Error in getting sparkSession" + str(error_message))
            sys.exit(400)

    def read_data(self, spark, folder_path: str, file_format: str, schema: StructType) -> DataFrame:
        """
        This function reads data stored in flat files in either json or csv format and return a data frame
        :param spark:           spark session object
        :param folder_path:     Path of the file
        :param file_format:     Format of the data file e.g. csv, json
        :param schema:          schema of the data in file
        :return:                Data frame that is returned by reading data file
        """
        self.logger.info(f"reading {file_format} data")
        data_frame = spark.read.format(file_format).option("header", "true") \
            .option("inferSchema", "true").schema(schema).load(folder_path)
        return data_frame
