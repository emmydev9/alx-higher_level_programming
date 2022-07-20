#!/usr/bin/python3
"""
A module to implement a square class with private attribute size
"""


class Square:
    """
    A class to implement a square
    """
    def __init__(self, size):
        """
        Initialize method to store the size of a square

        Args:
        param1 (int) - size of a square.
        """
        self.__size = size
