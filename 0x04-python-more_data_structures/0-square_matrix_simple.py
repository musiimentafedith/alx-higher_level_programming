#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        return ([list(map(lambda m: m * m, row)) for row in matrix ])
