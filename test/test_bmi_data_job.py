# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     27/01/23 12:33 am
# File:             test_bmi_data_job.py
# -----------------------------------------------------------------------
import unittest

from src.utils import spark_utils
from src.config import config_utils


class TestBMIJob(unittest.TestCase):

    """
    TODO: Add test for all functions. Currently it is skeleton only
    """

    utils = spark_utils.SparkUtils()
    spark = utils.get_spark_session("bmi_data_job")

    config_path = "../src/config/pipeline.cfg"
    configutil = config_utils.ConfigUtil(config_path)
    configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")

    def test_calculate_bmi(self):
        pass

    def test_get_bmi_category(self):
        pass

    def test_get_record_count(self):
        pass

    def test_run(self):
        pass
