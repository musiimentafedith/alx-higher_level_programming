#!/usr/bin/python3


"""

This module has a square class

"""


class Square:
    """

    This is a class representiong a square

    Attributes:
        __size (int): an int representing how big the square is

    """

    def __init__(self, size=0):
        """

        This is to initalise instances of the class

        Args:
            size (int): an int representing how big the square is

        """
        self.__size = size
    @property
    def size(self):
        """

        This method retrieves the size of the square

        Returns: size

        """
        return self.__size
    @setter
    def size(self, value):
        """

        This method sets the value os size

        Args:
            value (int): the value of size

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """

        This instance method returns the current square area

        Returns: area of the square

        """
        return self.__size ** 2

