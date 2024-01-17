#!/usr/bin/python3
"""Module for add_integer method"""


def add_integer(a, b=98):
    """Adds two integers. If only one argument
    is provided it returns the number itself.

    Args:
        a (int): The first integer to be added.
        b (int): The second integer to be added. Default is 98.

    Raises:
        TypeError: If either 'a' or 'b' are not of type int or float

    Returns:
        The sum of the two integers.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
