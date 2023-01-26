# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:39 pm
# File:             test_logging_utils.py.py
# -----------------------------------------------------------------------
import os
import unittest

from src.utils import config_utils
from src.utils.logging_utils import Logger

class TestLoggingUtils(unittest.TestCase):
    config_path = "../src/config/pipeline.cfg"
    configutil = config_utils.ConfigUtil(config_path)
    configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")

    def test_config_path(self):
        assert os.path.isfile(self.config_path) is True

    def test_config_utils(self):
        superman_landing_path = self.configutil.get_config("IO_CONFIGS", "AA_LANDING_PATH")
        random_user_landing_path = self.configutil.get_config("IO_CONFIGS", "AA_API_LANDING_PATH")
        print(os.path.abspath(superman_landing_path))
        assert superman_landing_path == "../../data/source_data/aa_data"
        assert random_user_landing_path == "../../data/source_data/aa_data/api_landing_path"

    def test_log_path():
        logger = Logger("test")
        log_path = logger.LOG_DIRECTORY
        print(log_path)
        absolute_path = os.path.abspath(log_path)
        print(absolute_path)


    def test_get_old_logs():
        """
        TODO: To complete this function
        :return:
        """


    def test_get_log_file_name():
        """
        TODO: To complete this function
        :return:
        """

    logger: Logger = Logger("test")
    path = os.path.abspath(logger.LOG_DIRECTORY)
    # logger.get_old_logs()
    logger.__get_file_names(logger, path)