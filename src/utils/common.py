# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     19/04/23 2:03 pm
# File:             common.py
# -----------------------------------------------------------------------


class DotDict(dict):
    """
    A dictionary that allows you to access and set values using dot notation.
        my_dict['foo'] = 'bar'
    becomes
        my_dict.foo = 'bar'
    """

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


class NestedDict:
    def __init__(self, dictionary):
        self._dictionary = dictionary

    def get(self, key):
        keys = key.split('.')
        value = self._dictionary
        for k in keys:
            value = value.get(k)
            if value is None:
                return None
        return value

    def set(self, key, value):
        keys = key.split('.')
        nested_dict = self._dictionary
        for k in keys[:-1]:
            nested_dict = nested_dict.setdefault(k, {})
        nested_dict[keys[-1]] = value
