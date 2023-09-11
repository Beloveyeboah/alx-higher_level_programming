#!/usr/bin/python3

"""Define Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    function to find area of square"""

    def __init__(self, size):
        """arg: size"""

        """Initialize a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
