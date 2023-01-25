# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 1:09 am
# File:             BMI_data_job.py
# -----------------------------------------------------------------------
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

            input_df = read_input_json_data(self.spark('BMI Calculator Challenge'),
                                            read_config("Paths", "input_file_path"))
            logger.info("dataframe from input json files created")

            bmi_df = calculate_bmi(input_df)
            logger.info("BMI Calculated")

            bmi_category_df = get_bmi_category(bmi_df)
            logger.info("BMI Category and Health risk derived")

            people_count = get_record_count(bmi_category_df)
            logger.info("Total number of people with overweight category: {}".format(people_count))

            write_csv_output(partition_folder_path(read_config("Paths", "output_file_path")), bmi_category_df)
            logger.info("Data processing completed")

        except Exception as message:
            logger.info("Failed to process the input file")
            logger.exception("Error in main driver function " + str(message))
            sys.exit(400)

if __name__ == "__main__":
    run()