# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     12/01/23 6:07 am
# File:             aa_data_job.py
# -----------------------------------------------------------------------
from src.app.job import Job
from src.data_jobs.aa_helper import AirAHelper
from src.utils import spark_utils
from src.utils.logging_utils import Logger


class AirADataJob(Job):
    def __int__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")
        self.aa_helper = AirAHelper(self.spark)

    logger = Logger(__name__).get_logger()
    url = "https://randomuser.me/api/0.8/?results=100"
    json_url = "https://gitlab.com/im-batman/simple-data-assestment/-/raw/main/superman.json"



