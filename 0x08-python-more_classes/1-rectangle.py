#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = height
            self._Rectangle__width = width


@property
def width(self):
    """getter for the private instance attribute width"""
    return self.__width


@width.setter
def width(self, value):
    """setter for the private instance with width"""
    if type(value) is not int:
        raise TypeError("width must be an integer")
    elif value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@property
def height(self):
    """getter for the private instance attribute height"""
    return self.__height


@height.setter
def height(self, value):
    """setter for the private instance with height"""
    if type(value) is not int:
        raise TypeError("height must be an integer")
    elif value < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
