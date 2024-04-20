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

    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.size):
            print("#"*self.size)
