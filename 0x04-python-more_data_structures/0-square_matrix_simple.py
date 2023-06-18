#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for sub in matrix:
        result = list(map(lambda x: x**2, sub))
        new_matrix.append(result)
    return new_matrix
