#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    Computes and returns a new matrix with each value equal to
    the square of the value of the input
    """
    return list(map(lambda sub: list(map(lambda x: x ** 2, sub)), matrix))
