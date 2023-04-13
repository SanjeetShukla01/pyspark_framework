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

    def test_config_path(self):
        assert os.path.isfile(self.config_path) is True

    def test_config_utils(self):
        superman_landing_path = self.configutil.get_config(
            "IO_CONFIGS", "AA_LANDING_PATH"
        )
        random_user_landing_path = self.configutil.get_config(
            "IO_CONFIGS", "AA_API_LANDING_PATH"
        )
        print(os.path.abspath(superman_landing_path))
        assert superman_landing_path == "../../data/source_data/aa_data"
        assert (
            random_user_landing_path
            == "../../data/source_data/aa_data/api_landing_path"
        )
