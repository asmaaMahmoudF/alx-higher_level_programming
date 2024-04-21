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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
         not all(isinstance(i, int) for i in value) or \
         value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" "*self.position[0] + "#"*self.size)

    def __str__(self):
        square_str = ""
        if self.size == 0:
            return square_str

        for i in range(self.position[1]):
            square_str += "\n"

        for i in range(self.size):
            square_str += " "*self.position[0] + "#"*self.size+"\n"

        return square_str [:-1]  # remove the last '\n'
