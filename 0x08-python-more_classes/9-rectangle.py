#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

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
            self.height = height
            self.width = width
            Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance with width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance with height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeters of a rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2*(self.width+self.height)

    def __str__(self):
        """method string object"""
        if self.width == 0 or self.height == 0:
            return ""
        for i in range(self.height - 1):
            print(str(self.print_symbol) * self.width)
        return str(self.print_symbol) * self.width

    def __repr__(self):
        """repr method"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """delet object/instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger or equal instance """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with size for width and height"""
        if size:
           return cls(size, size)
        else:
            pass