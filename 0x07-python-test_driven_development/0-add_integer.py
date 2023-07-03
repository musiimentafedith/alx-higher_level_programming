#!/usr/bin/python3

"""

in this module, i write a function that adds two integers.

"""


def add_integer(a, b=98):

    """
    This function adds two integers
    loats are type cast to int first before they are added.

    raises:
        TypeError, if are none float or int is added

    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return (a + b)
