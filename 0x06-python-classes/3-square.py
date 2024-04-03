#!/usr/bin/python3
"""a class square that defines a square """


class Square:
    """ class square """
    def __init__(self, size=0):
        """Initialaze a square based on 2-square.py
         args:
            size: representing the size of the square"
         Raise:
            TypeError:("size must be an integer")
            ValueError('size must be >= 0')
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculate the area of the square
        Return:
            the area of the square.
        """
        return(self.__size ** 2)
