# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 6:09 pm
# File:             aa_helper.py.py
# -----------------------------------------------------------------------
import urllib.request

from pyspark.sql.functions import explode, col, to_utc_timestamp, current_timestamp

from src.utils.column_constants import Columns
from src.utils.logging_utils import Logger


class AaHelper:
    def __init__(self, spark):
        self.spark = spark

    logger = Logger(__name__).get_logger

    def ingest_api_data(self, url, landing_path):
        """
        This function reads data from api endpoint into spark dataframe and stores on given path
        :param url:             API url
        :param landing_path:    path on local system to store data
        """
        try:
            json_api_data = urllib.request.urlopen(url).read().decode('utf-8')
            rdd = self.spark.sparkContext.parallelize([json_api_data])
            df = self.spark.read.json(rdd)
            final_df = df.select(explode(col("results")).alias("results")).select("results.user.email",
                                                                                  "results.user.gender",
                                                                                  "results.user.location.city",
                                                                                  "results.user.location.state",
                                                                                  "results.user.name.last",
                                                                                  "results.user.phone",
                                                                                  "results.user.registered",
                                                                                  "results.user.username",
                                                                                  "results.user.dob"
                                                                                  )\
                .withColumn(Columns.CURRENT_TIME, to_utc_timestamp(current_timestamp(), 'Asia/Kuala_lumpur'))
            final_df.coalesce(1).write.format('csv').mode('overwrite').option('header', True).option('sep', ',')\
                .save(landing_path)
        except Exception as exp:
            self.logger.error(f"error in reading api data {str(exp)}")



