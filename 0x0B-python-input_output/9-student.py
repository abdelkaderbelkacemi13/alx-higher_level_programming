#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """student details"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ a function that returns the dictionary of student"""
        return (self.__dict__)
