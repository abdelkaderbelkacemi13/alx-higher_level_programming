#!/usr/bin/python3
"""
we will define a class representing a Rectangle.
"""


class Rectangle:
    """
    this class  is representing a Rectangle based on 2-rectangle.py.
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
        return(self.__width)

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
        return(self.__height)

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calculation of the area of the rectangle
        """
        return(self.__height * self.__width)

    def perimeter(self):
        """
        calulation of the perimeter of the rectangle
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        return((self.__height + self.__width) * 2)

    def __str__(self):
        """
        print the rectangle using "#" character.
        """
        if (self.__height == 0 or self.__width == 0):
            return ("")
        printed_rectangle = ""
        for col in range(self.__height - 1):
            for row in range(self.__width):
                printed_rectangle += "#"
            if (col < self.__height - 1):
                printed_rectangle += "\n"
        return(printed_rectangle)
