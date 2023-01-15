# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 6:09 pm
# File:             aa_helper.py.py
# -----------------------------------------------------------------------
import os
import urllib.request

from pyspark.sql import DataFrame
from pyspark.sql.functions import explode, col, to_utc_timestamp, current_timestamp

from src.utils.column_constants import Columns
from src.utils.logging_utils import Logger


class AirAHelper:
    def __init__(self, spark):
        self.spark = spark

    logger = Logger(__name__).get_logger()
    logger.info("inside air helper")

    def ingest_api_data(self, url: str, landing_path: str) -> DataFrame:
        """
        This function reads data from api endpoint into spark dataframe and stores on given path
        :param url:             API url
        :param landing_path:    path on local system to store data
        :return Dataframe:      returns spark dataframe of data ingested from api
        """
        self.logger.info("reading random user data")
        try:
            api_data = urllib.request.urlopen(url).read().decode('utf-8')
            rdd = self.spark.sparkContext.parallelize([api_data])
            df = self.spark.read.json(rdd)

            self.logger.info("selected columns from read dataframe")

            final_df = df.select(explode(col("results")).alias("results"))\
                .select("results.user.email",
                        "results.user.gender",
                        "results.user.location.city",
                        "results.user.location.state",
                        "results.user.name.last",
                        "results.user.phone",
                        "results.user.registered",
                        "results.user.username",
                        "results.user.dob")\
                .withColumn(Columns.CURRENT_TS, current_timestamp())

            # TODO: Change current_ts column to MYT timezone
            # TODO: Implement column constants

            self.logger.info("creating final df")
            final_df.coalesce(1).write.format('csv').mode('overwrite')\
                .option('header', True).option('sep', ',')\
                .save(landing_path)

        except Exception as exp:
            self.logger.error(f"error in reading api data {str(exp)}")
            exit(1)
            raise
        return final_df

    def read_json_from_web(self, url: str, landing_path: str) -> None:
        """
        Reads data from given url, stores at a path
        :param url:                 Web address of the json file to be read
        :param landing_path:        Path on the local system to store ingested json data
        :return:                    Returns a spark dataframe
        """
        self.logger.info(f"reading data from {url}")
        response = urllib.request.urlopen(url)
        js = response.read()
        file_name = landing_path + "/superman.json"
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, "wb") as file:
            file.write(js)




