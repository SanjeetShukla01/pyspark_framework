# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:39 pm
# File:             test_logging_utils.py.py
# -----------------------------------------------------------------------
import os
import unittest
from src.utils.logging_utils import Logger


class TestLoggingUtils(unittest.TestCase):
    def test_log_path(self):
        logger = Logger("test")
        log_path = logger.LOG_DIRECTORY
        print(log_path)
        absolute_path = os.path.abspath(log_path)
        print(absolute_path)
        rel_path = os.path.relpath(log_path)
        assert rel_path == "../logs"

    def test_get_old_logs(self):
        """
        TODO: To complete this function
        :return:
        """

    def test_get_log_file_name(self):
        """
        TODO: To complete this function
        :return:
        """


if __name__ == "__main__":
    unittest.main()
