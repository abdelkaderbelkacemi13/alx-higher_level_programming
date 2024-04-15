#!/usr/bin/python3
"""BaseGeometry class (based on task 9. Full rectangle)"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ representing a rectangle"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """claculate the area of a square"""
        return (self.__size ** 2)
