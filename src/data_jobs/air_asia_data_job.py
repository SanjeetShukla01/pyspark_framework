# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     12/01/23 6:07 am
# File:             air_asia_data_job.py
# -----------------------------------------------------------------------
import os
import re

from pyspark import F
from pyspark.sql.functions import split, count

from src.app.job import Job
from src.config import etl_config
from src.data_jobs.air_asia_helper import AirAHelper
from src.utils import spark_utils, config_utils
from src.utils.column_constants import Columns
from src.utils.logging_utils import Logger


class AirADataJob(Job):
    def __init__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")
        self.aa_helper = AirAHelper(self.spark)

    logger = Logger(__name__).get_logger()
    configutil = config_utils.ConfigUtil()
    print(configutil.cfg_path)
    superman_landing_path = configutil.get_config("IO_CONFIGS", "AA_LANDING_PATH")
    random_user_landing_path = configutil.get_config("IO_CONFIGS", "AA_API_LANDING_PATH")

    superman_target_path = configutil.get_config("IO_CONFIGS", "AA_TARGET_PATH")
    random_user_target_path = configutil.get_config("IO_CONFIGS", "AA_TARGET_PATH")

    url = configutil.get_config("IO_CONFIGS", "AA_RANDOM_USER_URL")
    # "https://randomuser.me/api/0.8/?results=100"

    json_url = configutil.get_config("IO_CONFIGS", "AA_SUPERMAN_JSON_URL")
    # "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json"

    # TODO: Get rid of config file and use Enum instead.
    # TODO: Use classes to store and return data of custom type

    def run(self):
        try:
            config = getattr(etl_config, self.job_name)

            # Read the nested json file from url and process it.
            self.logger.info(f"reading superman.json file from web")
            self.aa_helper.read_json_from_web(self.json_url, self.superman_landing_path)
            self.logger.info(f"superman.json file stored at {self.superman_landing_path}")
            json_list = self.flatten_json(self.superman_landing_path)
            self.process_json(json_list, self.superman_target_path)

            # Read data from random user API.
            self.logger.info(f"Reading random user data from API")
            self.aa_helper.ingest_api_data(self.url, self.random_user_landing_path)
            self.logger.info(f"dataset dumped on {self.random_user_landing_path}")

            self.process_api_data(self.random_user_landing_path, self.random_user_target_path)
            self.logger.info(f"placed process data at {self.random_user_target_path}")

        except Exception as exp:
            self.logger.error(f"An error occurred while running the pipeline {str(exp)}")
            raise

    def flatten_json(self, path: str) -> list:
        """
        reads json file and flattens data based on regex rule
        :param path:        Path of the json file
        :return:            returns flattened json list
        """
        self.logger.info(f"flattening json data")
        with open(path + '/superman.json', encoding='utf-8') as f:
            r = re.split('(\{.*?\})(?= *\{)', f.read())
        event_list = []
        for ele in r:
            each = ele.splitlines()
            event_list.extend(each)
        sorted_event_list = sorted(event_list, key=lambda x: x[0])
        return sorted_event_list

    def process_json(self, json: list, path: str):
        """
        :param json:        Json data to be processed
        :param path:        Path of the json file
        :return:            returns flattened json list
        """
        self.logger.info(f"processing json data")
        unique = {repr(each): each for each in json}.values()
        try:
            filename = path + "/superman_final.json"
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'w', encoding='utf-8') as f:
                for d in unique:
                    f.write(d + '\n')
            self.logger.info("superman_final.json has been created")
        except IOError as exp:
            self.logger.error(f"error reading json file {str(exp)}")
            raise

    def process_api_data(self, input_path, output_path):
        """
        :return:            writes data to csv and returns a dataframe
        """
        self.logger.info(f"processing api data")
        try:
            df = self.spark.read.format("csv").option("header", "true").load(input_path)
            df1 = df.select(Columns.GENDER, split("email", "@")[1].alias("email_provider"), "username")
            df2 = df1.groupby("gender", "email_provider").agg(count("username"))
            df2.coalesce(1).write.format('csv').mode('overwrite').option('header', True).option('sep', ',')\
                .save(output_path + '/assessment_2_total_count')
        except IOError as exp:
            self.logger.error(f"error reading json file {str(exp)}")
            raise


# if __name__ == "__main__":
#     air_data_job: AirADataJob = AirADataJob("aa_data_job")
#     air_data_job.run()

