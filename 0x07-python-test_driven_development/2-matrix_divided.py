#!/usr/bin/python3

"""
This module includes a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):

    """
    divides all elements of a matrix
    Returns:
            a new matrix
    """

    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(matrix[i], list) or matrix[i] == []:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for j in range(len(matrix[0])):
            if not isinstance(matrix[i][j], float) and not isinstance(matrix[i][j], int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


    result = (list(map(lambda y: round(y/div, 2), row)) for row in matrix)

    return list(result)


