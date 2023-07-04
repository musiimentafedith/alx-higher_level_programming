#!/usr/bin/python3

"""

This module includes a say_my_name function

"""


def say_my_name(first_name, last_name=""):

    """

    This function prints My name is <first name> <last name>
    args:
        first_name(str)
        last_name(str)
    raises:
        TypeError if any of firs or last name is not string

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
