# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 9:05 am
# File:             test_config_utils.py
# -----------------------------------------------------------------------
import os
import unittest
from src.utils import config_utils


class TestConfigUtils(unittest.TestCase):
    config_path = "../src/config/pipeline.cfg"
    configutil = config_utils.ConfigUtil(config_path)
    configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")

    def test_print_config(self):
        # path = self.configutil.get_config("IO_CONFIGS", "INPUT_DATA_PATH")
        if os.path.isfile(self.config_path):
            print(self.config_path)
        else:
            print("Not exist")

    # def test_config_utils(self):
    #     superman_landing_path = self.configutil.get_config("IO_CONFIGS", "AA_LANDING_PATH")
    #     random_user_landing_path = self.configutil.get_config("IO_CONFIGS", "AA_API_LANDING_PATH")
    #     # assert superman_landing_path == expected_df.count()
    #     print(superman_landing_path)
    #     print(random_user_landing_path)
    #
    # def test_config_path(self):
    #     config_path = "../config/pipeline.cfg"
    #     print(config_path)
