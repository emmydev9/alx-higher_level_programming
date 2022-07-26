#!/usr/bin/python3

'''A class about rectangle'''


class Rectangle:
    '''A rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initialization of class
        Args:
            width: width of the Rectangle
            height: height of the Rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''a getter attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''a setter attribute'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """a getter attribute for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """a setter attribute for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ public instance function return the area
            of the rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ public instance function return the
            perimeter of the rectangle"""
        if self.__width and self.__height:
            return (2 * (self.__width + self.height))
        else:
            return (0)

    def __str___(self):
        """ method that return the Rectangle #

        Return : str representation of the rectangle
        """
        rectange = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            rectangle += ("#" * self.__width) + "#"

            return (rectangle[:-1])
