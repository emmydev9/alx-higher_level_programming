#!/usr/bin/python3
'''A class about rectangle'''


class Rectangle:
    '''A rectangle class'''
    def __init__(self, width=0, height=0):
        '''Initialization of class'''
        pass

    @property
    def width(self):
    	'''a getter attribute'''
    	return self.width

    @width.setter
    def width(self, value):
    	'''a setter attribute'''
    	if is not isinstance(value, int):
    		return TypeError("width must be an integer")
    	elif value < 0:
    		return ValueError("width must be >= 0")
    	else:
    		self.width = value
    @property
    def height(self):
    	"""a getter attribute for height"""
    	return self.height

    @height.setter
    def height(self, value):
    	"""a setter attribute for height"""
    	if is not isinstance(value, int):
    		return TypeError("height must be an integer")
    	elif value < 0:
    		return ValueError("")

