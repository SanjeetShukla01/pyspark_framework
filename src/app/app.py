# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 9:19 pm
# File:             app.py.py
# -----------------------------------------------------------------------
import argparse
import datetime
import importlib
import os
import sys
import time

from src.app.job_factory import JobFactory
from src.utils.logging_utils import Logger

sys.path.append(os.path.abspath(os.path.dirname(__file__)))


class App:
    logger = Logger(__name__).get_logger()
    logger.info("inside app.py")

    def run(self, job_name: str) -> None:
        self.logger.info("Run given job name")
        start = time.time()
        try:
            # module = importlib.import_module(f"JobFactory(job_name)")
            module = JobFactory(job_name).factory()
            self.logger.info("job crated using job factory")
            module.run()
            end = time.time()
            self.logger.info(f"execution of job {job_name} took {end - start} seconds")
        except Exception as ex:
            self.logger.info(str(datetime.datetime.now()) + "________Abruptly Exited__________")
            raise Exception(f"Execution of job: {job_name} failed with msg {ex}")


def setup_parser():
    parser = argparse.ArgumentParser(description="args for pyspark app")
    parser.add_argument('--job-name',
                        nargs='?',
                        type=str,
                        default="air_asia_data_job",
                        # required=True,
                        help="job name to be invoked"
                        )
    return parser


if __name__ == "__main__":
    arg_parser = setup_parser()
    args = arg_parser.parse_args()
    app = App()
    app.run(args.job_name)


