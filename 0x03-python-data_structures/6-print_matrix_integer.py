#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for pub in matrix:
        for sub in row:
            print("{:d}".format(col), end=" " if sub != pub[-1] else "")
        print()
