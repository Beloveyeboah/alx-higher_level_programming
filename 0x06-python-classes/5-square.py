#!/usr/bin/python3

"""Creating a class Square"""


class Square:
    """creating class of square"""

    def __init__(self, size=0):
        """self refrence"""
        self.__size = size

    @property
    def size(self):
        """determine size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculating area"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints the square"""

        for arr in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.size == 0:
            print("")
