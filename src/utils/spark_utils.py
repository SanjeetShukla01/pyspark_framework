from pyspark.sql import SparkSession


class SparkUtils:
    def get_spark_session(self, app_name: str) -> SparkSession:
        """
        This function creates spark session
        :param app_name:    Name of the pyspark app to be returned for SparkSession
        :return:            Returns SparkSession
        """
        try:
            spark_session = SparkSession.builder.appName(app_name).enableHiveSupport().getOrCreate()
            return spark_session
        except Exception as error_message:
            logger.info(" Failed to create sparkSession")
            logger.exception("Error in getting sparkSession" + str(error_message))
            sys.exit(400)
