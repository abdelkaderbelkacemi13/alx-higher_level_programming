#!/usr/bin/python3
"""BaseGeometry class (based on task 8. Rectangle)"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representing the rectangle using BaseGeomtry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """claculate the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """Representing the Rectangle"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
