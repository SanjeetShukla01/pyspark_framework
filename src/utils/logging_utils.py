# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     12/01/23 6:22 am
# File:             logging_utils.py
# -----------------------------------------------------------------------
import logging
import os.path
import pathlib
import sys
import threading
from datetime import datetime


class SingletonDoubleChecked(object):
    """
    In python 2x having object in class definition means new style class.
    In python 3x this is not needed.
    """

    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # defining the class method
    @classmethod
    def get_instance(cls):
        with cls.__singleton_lock:
            if not cls.__singleton_instance:
                cls.__singleton_instance = cls()
        return cls.__singleton_instance


class Logger(SingletonDoubleChecked):
    # Maximum number of logs to store
    LOGS_COUNT = 10

    def __init__(self, logger_name):
        """
        Constructor, takes logger_name as an argument and an option argument days_to_keep(default=3days)
        logs older than current_date-days_to_keep will be erased
        :param      logger_name:    Name of the logger to give context of the class where log is generated
        """
        self.FORMATTER = logging.Formatter(
            "[%(levelname)s] - %(asctime)-15s (%(relativepath)s:%(lineno)d): %(message)s",
            datefmt="%m/%d/%Y %I:%M:%S %p",
        )
        self.LOG_DIRECTORY = os.path.join(
            os.path.dirname(__file__), "../../logs/"
        )
        if not os.path.exists(self.LOG_DIRECTORY):
            os.mkdir(self.LOG_DIRECTORY)
        self.FILE_NAME = datetime.now().strftime("log_%d-%m-%Y-%H:%M:%S.log")
        self.LOG_FILE = self.LOG_DIRECTORY + self.FILE_NAME
        self.logger_name = logger_name
        # self.__clean_old_logs()

    def get_console_handler(self) -> logging.StreamHandler:
        """
        this function returns the console handler for logger
        :return:    returns StreamHandler object for console logger
        """
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        console_handler.addFilter(PackagePathFilter())
        return console_handler

    def get_file_handler(self) -> logging.FileHandler:
        """
        :return:    returns FileHandler with rotating log file configuration
        """
        file_handler = logging.FileHandler(self.LOG_FILE)
        file_handler.setFormatter(self.FORMATTER)
        file_handler.addFilter(
            PackagePathFilter()
        )  # this adds relative path to the handler
        return file_handler

    def get_logger(self) -> logging.Logger:
        """
        :return: Logger object with handler and file rotation
        """
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.INFO)
        logger.addHandler(self.get_console_handler())
        logger.addHandler(self.get_file_handler())
        logger.propagate = False
        return logger

    def __clean_old_logs(self):
        for name in self.__get_old_logs():
            path = os.path.join(self.LOG_DIRECTORY, name)
            self.__delete_files(self, path)

    def __get_old_logs(self):
        logs = [name for name in self.__get_file_names()]
        logs.sort(reverse=True)
        return logs[self.LOGS_COUNT :]

    def __get_file_names(self):
        return [
            item.name
            for item in pathlib.Path(self.LOG_DIRECTORY).glob("*")
            if item.is_file()
        ]

    @staticmethod
    def __delete_files(self, path):
        try:
            os.remove(path)
        except Exception as ex:
            print("Exception deleting log file" + str(ex))


class PackagePathFilter(logging.Filter):
    """
    This class is used to add relative path to the logs
    """

    def filter(self, record: logging.LogRecord) -> bool:
        """
        this method is used to filter log records and make the path relative in log records
        :param record:          log record
        :return:                returns boolean
        """
        pathname = record.pathname
        record.relativepath = None
        abs_sys_path = map(os.path.abspath, sys.path)
        for path in sorted(abs_sys_path, key=len, reverse=True):
            if not path.endswith(os.sep):
                path += os.sep
            if pathname.startswith(path):
                record.relativepath = os.path.relpath(pathname, path)
                break
        return True


if __name__ == "__main__":
    logger: Logger = Logger("test")
    path = os.path.abspath(logger.LOG_DIRECTORY)
