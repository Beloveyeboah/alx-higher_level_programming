#!/usr/bin/python3

# CREATED BY BELOVEYEBOAH

"""A class that defines a rectangle"""


class Rectangle:
    """creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Args:
        width is an integer
        height also an integer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """links width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width atrribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """seeks height attributes"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
