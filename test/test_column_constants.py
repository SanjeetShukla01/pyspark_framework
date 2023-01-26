# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     15/01/23 10:46 pm
# File:             test_column_constants.py
# -----------------------------------------------------------------------
import unittest

from src.utils.column_constants import Columns


class TestColumnConstants(unittest.TestCase):
    def test_column_constants(self):
        col_current_ts = Columns.CURRENT_TS
        print(col_current_ts)
        assert col_current_ts == "current_ts"

