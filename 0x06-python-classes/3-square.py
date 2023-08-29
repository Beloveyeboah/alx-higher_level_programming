#!/usr/bin/python3

"""Creating a class Square"""


class Square:
    """creating class of square"""

    def __init__(self, size=0):
        """self refrence"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """calculating area"""
        return (self.__size * self.__size)
