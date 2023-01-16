# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 9:19 pm
# File:             job_factory.py
# -----------------------------------------------------------------------
from src.data_jobs.BMI_data_job import BMIDataJob
from src.data_jobs.air_asia_data_job import AirADataJob
from src.data_jobs.happiness_index_data_job import HappinessIndex
from src.data_jobs.william_hills_data_job import WHDataJob
from src.utils.logging_utils import Logger


class JobFactory:
    def __init__(self, job_name):
        self.job_name = job_name

    logger = Logger(__name__).get_logger()

    def factory(self):
        job = None
        if self.job_name == 'air_asia_data_job':
            self.logger.info("Creating AirAData Job")
            job = AirADataJob(self.job_name)
        elif self.job_name == 'happiness_index_job':
            self.logger.info("Creating HappinessIndex Job")
            job = HappinessIndex(self.job_name)
        elif self.job_name == 'bmi_data_job':
            self.logger.info("Creating BMI Data Job")
            job = BMIDataJob(self.job_name)
        elif self.job_name == 'wh_data_job':
            self.logger.info("Creating WH Data Job")
            job = WHDataJob(self.job_name)
        else:
            raise ValueError("Bad job name: {}".format(self.job_name))
        return job
