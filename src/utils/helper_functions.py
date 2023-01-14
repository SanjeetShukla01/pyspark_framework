# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:15 pm
# File:             helper_functions.py
# -----------------------------------------------------------------------
import datetime
import os

from src.utils.logging_utils import Logger


class Helper:
    logger = Logger(__name__).get_logger()

    @staticmethod
    def get_nth_parent_folder(file_path, n):
        for i in range(n):
            file_path = os.path.dirname(file_path)
        return os.path.basename(file_path)

    def get_partitioned_output_path(self, file_path):
        """
        This functions takes path as argument and returns
        partitioned subdirectory to store date partitioned on date
        :param file_path:           path of the output file
        :return:                    returns actual partitioned path to store output data to
        """
        file_path = file_path + '/' + str(datetime.datetime.today().year) + '/' \
                    + str(datetime.datetime.today().month) + '/' + str(datetime.datetime.today().day)
        self.logger.info(f"file_path: {file_path}")
        return file_path
