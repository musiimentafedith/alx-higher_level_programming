#!/usr/python3

""" class that defines a rectangle """


class Rectangle:

    """ defines a rectagle """

    def __init__(self, width=0, height=0):
        """ intialize a new rectagle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter method"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
