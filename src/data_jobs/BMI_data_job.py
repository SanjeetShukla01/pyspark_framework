# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 1:09 am
# File:             BMI_data_job.py
# -----------------------------------------------------------------------
import sys

from src.app.job import Job
from src.utils import spark_utils, config_utils
from src.utils.logging_utils import Logger
from pyspark.sql.functions import round, when, col


class BMIDataJob(Job):
    def __init__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("BMI_data_job")

    logger = Logger(__name__).get_logger()
    configutil = config_utils.ConfigUtil()
    utils = spark_utils.SparkUtils()
    bmi_data = configutil.get_config("IO_CONFIGS", "BMI_DATA")
    bmi_data_target = configutil.get_config("IO_CONFIGS", "BMI_DATA_TARGET")

    def calculate_bmi(self, df):
        """
        This function calculates height in meters and BMI value for the input dataframe.
        :param df: raw input dataframe for which the BMI will be calculated.
        :return: dataframe with height in meters,BMI value added to the input dataframe
        """
        self.logger.info(f"calculating Height in Meter and BMI")
        return df.withColumn('HeightM', df.HeightCm / 100).withColumn('BMI', round(
            df.WeightKg / ((df.HeightCm / 100) * (df.HeightCm / 100)), 2))

    def get_bmi_category(self, df):
        """
        This function adds the BMI category and Health risk based on the BMI value
        :param df: input dataframe with BMI values
        :return: Dataframe with  BMI category and Health risk derived from their respective BMI values
        """
        self.logger.info(f"Creating new column BMI Category")
        return df.withColumn('BMI Category', when(df.BMI <= 18.4, "Underweight")
                             .when((df.BMI >= 18.5) & (df.BMI <= 24.9), "Normal weight")
                             .when((df.BMI >= 25) & (df.BMI <= 29.9), "Overweight")
                             .when((df.BMI >= 30) & (df.BMI <= 34.9), "Moderately obese")
                             .when((df.BMI >= 35) & (df.BMI <= 39.9), "Severely obese")
                             .when((df.BMI >= 40), "Very severely obese")
                             .otherwise('Undefined')) \
            .withColumn('Health risk', when(df.BMI <= 18.4, "Malnutrition risk")
                        .when((df.BMI >= 18.5) & (df.BMI <= 24.9), "Low risk")
                        .when((df.BMI >= 25) & (df.BMI <= 29.9), "Enhanced risk")
                        .when((df.BMI >= 30) & (df.BMI <= 34.9), "Medium risk")
                        .when((df.BMI >= 35) & (df.BMI <= 39.9), "High risk")
                        .when((df.BMI >= 40), "Very high risk")
                        .otherwise('Undefined'))

    def get_record_count(self, df):
        """
        This function returns the count of people who are in 'Overweight' category
        :param df: dataframe with BMI value and their respective BMI categories
        :return: Count of records of people with BMI category as 'Overweight'
        """
        self.logger.info(f"Applying filter to the dataframe to fetch only Overweight records")
        return df.filter(col("BMI Category") == 'Overweight').count()

    def run(self):
        """
        Driver function to run the spark application.
        :return:
        """
        try:

            input_df = self.utils.read_data(self.spark, self.bmi_data, "json")
            self.logger.info(f"Created dataframe: {input_df} from input json file")

            bmi_df = self.calculate_bmi(input_df)
            self.logger.info("Calculated BMI Based on predefined rule")

            bmi_category_df = self.get_bmi_category(bmi_df)
            self.logger.info("Calculated BMI Category and Health risk based on predefined rule")

            people_count = self.get_record_count(bmi_category_df)
            self.logger.info("Total number of people in overweight category: {}".format(people_count))

            self.utils.write_data(bmi_category_df, self.bmi_data_target, "json")
            self.logger.info("Data processing completed")

        except Exception as message:
            self.logger.info("Failed to process the input file")
            self.logger.exception("Error in main driver function " + str(message))
            sys.exit(400)


# if __name__ == "__main__":
#     bmi_data_job: BMIDataJob = BMIDataJob("bmi_data_job")
#     bmi_data_job.run()
