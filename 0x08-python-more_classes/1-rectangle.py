#!/usr/bin/python3
"""
we will define a class representing a Rectangle.
"""


class Rectangle:
    """
    this class  is representing a Rectangle based on 0-rectangle.py.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle
        Args:
            width; an int represent the width of the rectangle.
            height: an int represent the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        set the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        set the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
