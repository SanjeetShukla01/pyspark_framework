# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 11:30 pm
# File:             happiness_index_data_job.py
# -----------------------------------------------------------------------
from src.app.job import Job
from src.utils import spark_utils, config_utils
from src.utils.logging_utils import Logger


class HappinessIndex(Job):
    def __init__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")

    logger = Logger(__name__).get_logger()
    configutil = config_utils.ConfigUtil()
