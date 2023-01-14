# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     12/01/23 6:10 am
# File:             job.py.py
# -----------------------------------------------------------------------

from abc import ABCMeta


class Job(metaclass=ABCMeta):
    def run(self):
        pass
