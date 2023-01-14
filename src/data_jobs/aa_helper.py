# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 6:09 pm
# File:             aa_helper.py.py
# -----------------------------------------------------------------------
from src.utils.column_constants import column_constants
from src.utils.logging_utils import Logger


class AaHelper:
    def __init__(self, spark):
        self.spark = spark

    logger = Logger(__name__).get_logger
    c = getattr(column_constants, "column_constants")

    def ingest_api_data(self, url, landing_path):
        """
        This function reads data from api endpoint into spark dataframe and stores on given path
        :param url:             API url
        :param landing_path:    path on local system to store data
        """


