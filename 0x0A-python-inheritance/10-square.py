#!/usr/bin/python3

# CREATED: BELOVE YEBOAH ISAAC

"""define squares"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherited from rectangle"""

    def __init__(self, size):
        """arg
        size
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
