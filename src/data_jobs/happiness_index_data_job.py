# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 11:30 pm
# File:             happiness_index_data_job.py
# -----------------------------------------------------------------------
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, lit, when

from src.app.job import Job
from src.utils import spark_utils, config_utils
from src.utils.logging_utils import Logger
from src.utils.table_schema import happiness_data_schema


class HappinessIndex(Job):
    def __init__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("happiness_index_data_job")

    logger = Logger(__name__).get_logger()
    configutil = config_utils.ConfigUtil()
    utils = spark_utils.SparkUtils()
    happiness_data = configutil.get_config("IO_CONFIGS", "HAPPINESS_INDEX_DATA")
    happiness_data_target = configutil.get_config("IO_CONFIGS", "HAPPINESS_INDEX_TARGET")

    def run(self):
        df_csv = self.utils.read_data(self.spark, self.happiness_data, "csv", happiness_data_schema)
        df2 = self.rename_columns(df_csv)
        df3 = self.correlation_transform(df2)
        df4 = self.generate_annotation(df3)
        df4.show()
        df4.coalesce(1).write.format('csv').mode('overwrite').option('header', True).option('sep', ',') \
            .save(self.happiness_data_target)

    def filter_data(self, df: DataFrame, number: int):
        self.logger.info(f"filtering dataframe to fetch {number} records")
        return df.filter(col("Happiness Rank") <= number)

    def rename_columns(self, df: DataFrame):
        """
        This function is intended to change the column name
        :param df:      Input Data Frame
        :return:        returns a dataframe after column name changed
        """
        self.logger.info(f"Renaming columns of Happiness Index data")
        for name in df.schema.names:
            df = df.withColumnRenamed(name, (name.replace(' ', '_').replace('(', '').replace(')', '').lower()))
        return df

    def correlation_transform(self, df: DataFrame):
        self.logger.info(f"Renaming columns of Happiness Index data")
        return df\
            .withColumn("c_happiness_life_exp", lit(round(df.corr("happiness_rank", "health_life_expectancy"), 2))) \
            .withColumn("c_happiness_generosity", lit(round(df.corr("happiness_rank", "generosity"), 2))) \
            .withColumn("c_happiness_corruption", lit(round(df.corr("happiness_rank", "trust_government_corruption"), 2))) \
            .withColumn("c_happiness_freedom", lit(round(df.corr("happiness_rank", "freedom"), 2))) \
            .withColumn("c_happiness_economy", lit(round(df.corr("happiness_rank", "economy_gdp_per_capita"), 2)))

    def generate_annotation(self, df: DataFrame):
        self.logger.info(f"Generating annotation columns for Happiness Index data")
        return df.withColumn("annotations", when(col("happiness_rank") <= 5, "Doing Well")
                             .when(col("happiness_rank") <= 10, "Still Good")
                             .when(col("happiness_rank") <= 50, "Could be Better")
                             .otherwise("What are you Doing"))


if __name__ == "__main__":
    happiness_index_job = HappinessIndex("happiness_index_job")
    happiness_index_job.run()
