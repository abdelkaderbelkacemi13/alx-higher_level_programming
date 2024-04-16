#!/usr/bin/python3
"""class Student based on (9-student.py)"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """student details"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ a function that returns the dictionary of student"""
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {ky: getattr(self, ky) for ky in attrs if hasattr(self, ky)}
        return(self.__dict__)
