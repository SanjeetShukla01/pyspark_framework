# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 9:57 pm
# File:             william_hills_data_job.py
# -----------------------------------------------------------------------
from src.app.job import Job
from src.utils import spark_utils, config_utils
from src.utils.logging_utils import Logger


class WHDataJob(Job):
    # TODO: Implement this completely
    def __init__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("wh_data_job")

    logger = Logger(__name__).get_logger()
    configutil = config_utils.ConfigUtil()

