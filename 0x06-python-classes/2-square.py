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
            self.__size = int(size)
