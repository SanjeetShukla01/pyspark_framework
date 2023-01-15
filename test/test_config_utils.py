# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 9:05 am
# File:             test_config_utils.py
# -----------------------------------------------------------------------
from src.utils import config_utils


def test_config_utils():
    configutil = config_utils.ConfigUtil()
    superman_landing_path = configutil.get_config("IO_CONFIGS", "AA_LANDING_PATH")
    random_user_landing_path = configutil.get_config("IO_CONFIGS", "AA_API_LANDING_PATH")
    print(superman_landing_path)
    print(random_user_landing_path)


def test_config_path():
    config_path = "../config/pipeline.cfg"
    print(config_path)
