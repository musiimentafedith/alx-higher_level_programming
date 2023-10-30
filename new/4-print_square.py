#!/usr/bin/python3

"""

This module includes a print_square function

"""


def print_square(size):

    """

    The function prints a square with the character #
    
    args:
        size(int) - length of the square

    Raises:
        TypeError if size is not an int
        ValueError if size is less than 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print("#"*size)
