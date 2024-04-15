#!/usr/bin/python3
"""is_same_class method"""


def is_same_class(obj, a_class):
    """check if the object is exactly an instance of the class"""
    return type(obj) == a_class
