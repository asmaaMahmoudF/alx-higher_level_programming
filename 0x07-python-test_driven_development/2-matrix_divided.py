#!/usr/bin/python3
"""Module for add_integer method

    Write a function that divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div):
    matrix must be a list of lists of integers or floats,
    otherwise raise a TypeError exception with the message
    matrix must be a matrix (list of lists)
    of integers/floats

    Each row of the matrix must be of the same size,
    otherwise raise a TypeError exception
    with the message Each row of the matrix must have
    the same size

    div must be a number (integer or float),
    otherwise raise a TypeError exception
    with the message div must be a number

    div can’t be equal to 0, otherwise raise a
    ZeroDivisionError exception
    with the message division by zero

    All elements of the matrix should be divided by div,
    rounded to 2 decimal places
    Returns a new matrix
    You are not allowed to import any module
"""


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
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
                             integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")
        if div is 0:
            raise ZeroDivisionError("division by zero")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                                 integers/floats")
    return [[round(x / div, 2) for x in row] for row in matrix]


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
