# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 11:55 am
# File:             test_aa_data_job.py
# -----------------------------------------------------------------------
from src.data_jobs.aa_data_job import AirADataJob
from src.data_jobs.aa_helper import AirAHelper
from src.utils import spark_utils


def test_aa_data_job():
    spark = spark_utils.SparkUtils().get_spark_session("aa_data_job")
    aa_helper: AirAHelper = AirAHelper(spark)
    air_data_job = AirADataJob()
    print(air_data_job.url)
    print(air_data_job.json_url)
    print(air_data_job.superman_landing_path)
    aa_helper.read_json_from_web(air_data_job.json_url, air_data_job.superman_landing_path)
    json_list = air_data_job.flatten_json(air_data_job.superman_landing_path)
    print(air_data_job.process_json(json_list, air_data_job.superman_target_path))
    aa_helper.ingest_api_data(air_data_job.url, air_data_job.random_user_target_path)

