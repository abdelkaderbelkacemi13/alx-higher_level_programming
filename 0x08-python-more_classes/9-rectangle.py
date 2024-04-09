#!/usr/bin/python3
"""
we will define a class representing a Rectangle.
"""


class Rectangle:
    """
    this class  is representing a Rectangle based on 2-rectangle.py.
    Attributes:
        number_of_instances: the number of active instances of the rectangle
        print_symbol: the sybol we will use to print the rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize the rectangle
        Args:
            width; an int represent the width of the rectangle.
            height: an int represent the height of the rectangle.

        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        set the width of the rectangle
        """
        return (self.__width)

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
        return (self.__height)

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
        return (self.__height * self.__width)

    def perimeter(self):
        """
        calulation of the perimeter of the rectangle
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """
        print the rectangle using different character.
        """
        if (self.__height == 0 or self.__width == 0):
            return ("")
        printed_rectangle = ""
        for col in range(self.__height):
            for row in range(self.__width):
                printed_rectangle += str(self.print_symbol)
            if (col < (self.__height - 1)):
                printed_rectangle += "\n"
        return (printed_rectangle)

    def __repr__(self):
        """
        return a string representation of the rectangle
         to be able to recreate a new instance by using eval()
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """
        Print the message "Bye rectangle..."
        when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns a new Rectangle instance with width == height == size
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if (rect_2.area() >= rect_1.area()):
            return (rect_2)
        return (rect_1)

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
