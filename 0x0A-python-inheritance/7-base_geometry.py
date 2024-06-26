#!/usr/bin/python3
"""BaseGeometry class (based on task 6. Improve Geometry)"""


class BaseGeometry:
    """representing a BaseGeometry class"""
    def area(self):
        """method to calculate the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:            
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
