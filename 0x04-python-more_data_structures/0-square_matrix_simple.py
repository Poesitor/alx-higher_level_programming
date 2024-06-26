#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """ Computes the square value of all integers in a matrix """

    return ([list(map(lambda x: x * x, row)) for row in matrix])
