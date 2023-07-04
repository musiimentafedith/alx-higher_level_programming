#!/usr/bin/python3

"""
This module includes a text_indentation function

"""


def text_indentation(text):

    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    """

    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in ".?:":
            continue
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
    print()

