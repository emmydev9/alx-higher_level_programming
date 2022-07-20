#!/usr/bin/python3
"""
A module that implements a Square
"""


class Square:
    """
    A square implementation
    """
    def __init__(self, size=0):
        """
        An initialization of the square with a private attribute

        Args:
        param1 (int) - size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A public method that returns the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        return the size of the Square Object
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        set the size of a square Object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
