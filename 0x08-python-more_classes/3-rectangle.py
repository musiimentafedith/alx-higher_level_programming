#!/usr/bin/python3

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

    def area(self):
        """ returns the area of a rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ returns perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ returns easy to read string with relative
        details of the object in this case '#'
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        temp = []
        for i in range(self.__height):
            for j in range(self.__width):
                temp.append('#')
            if i != self.__height - 1:
                temp.append('\n')
        return ("".join(temp))
