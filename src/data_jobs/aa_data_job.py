# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     12/01/23 6:07 am
# File:             aa_data_job.py
# -----------------------------------------------------------------------
from src.app.job import Job
from src.utils import spark_utils


class AirADataJob(Job):
    def __int__(self, job_name):
        self.job_name = job_name
        self.spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")


