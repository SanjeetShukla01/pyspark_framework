# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:39 pm
# File:             test_logging_utils.py.py
# -----------------------------------------------------------------------
import os

from src.utils.logging_utils import Logger


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