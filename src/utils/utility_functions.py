# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     13/01/23 7:15 pm
# File:             utility_functions.py
# -----------------------------------------------------------------------
import os


def get_nth_parent_folder(file_path, n):
    for i in range(n):
        file_path = os.path.dirname(file_path)
    return os.path.basename(file_path)
