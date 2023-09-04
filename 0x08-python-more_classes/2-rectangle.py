#!/usr/bin/python3

""""class that defines a rectangle"""

# CREATED BY BELOVEYEBOAH


class Rectangle:
    """creates a rectangle"""
    def __init__(self, width=0, height=0):
        """Args:
        width is an integer
        height also an integer"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrive width attribute of class"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrive heights attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
