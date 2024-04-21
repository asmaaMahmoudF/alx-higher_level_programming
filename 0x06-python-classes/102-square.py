#!/usr/bin/python3
"""Square Module """


class Square:
    """class Square """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value
        if value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        if isinstance(self, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(self, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(self, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(self, Square):
            return self.area() >= other.area()
        return NotImplemented
