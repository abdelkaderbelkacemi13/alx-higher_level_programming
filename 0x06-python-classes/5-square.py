#!/usr/bin/python3
"""a class square that defines a square """


class Square:
    """ class square """
    def __init__(self, size=0):
        """defines a square based on 4-square.py

         args:
            size: representing the size of the square"
        """
        self.__size = size

    @property
    def size(self):
        """def size(self): to retrieve the square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """property setter def size(self, value):
            to set the private attribute of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        calculate and return the area of the square.

        """
        return(self.__size * self.__size)

    def my_print(self):
        """def my_print(self): prints in stdout
        the square with the character #"""
        for i in range(self.__size):
            print("#" * self.__size, end="")
            if (self.__size == 0):
                print("")
            print()
