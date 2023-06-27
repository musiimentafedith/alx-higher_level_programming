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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """

        This instance method returns the current square area

        Returns: area of the square

        """
        return self.__size ** 2
