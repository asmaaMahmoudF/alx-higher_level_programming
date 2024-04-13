#!/usr/bin/python3
"""Module for add_integer method"""


def matrix_divided(matrix, div):
    """divided all elements of matrix by div.
    is provided it returns the number itself.

    Args:
        matrix : The list of lists containing int or float
        div : number to divide matrix by ...

    Raises:
        TypeError: If matrix is not list of lists containing int or float
        TypeError: if sublists are not all same size
        TypeError: if div is not int or float

    Returns:
        list : list of lists representing divided matrix.
    """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
                             integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                                 integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
