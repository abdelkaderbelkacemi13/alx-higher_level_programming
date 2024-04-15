#!/usr/bin/python3
"""inherits_from"""


def inherits_from(obj, a_class):
    """check if the object is a true subclass of a class"""
    return (isinstance(obj, a_class) and type(obj) != a_class)
