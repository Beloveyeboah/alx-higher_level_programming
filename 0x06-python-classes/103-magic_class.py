#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

import math


class MagicClass:
    """creats magic calculator"""

    def __init__(self, radius=0):

        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """return area"""
        return (self.__radius ** 2 * math.pi)
