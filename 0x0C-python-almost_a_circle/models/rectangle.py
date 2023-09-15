#!/usr/bin/python3


"""define class inheritance from base"""

from models.base import Base


class Rectangle(Base):
    """inherites from class base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """args list
            width
            height
            x
            y
            """

        self._width = width
        self._height = height
        self._x = x
        self._y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the attribute width"""

        return self._width

    @width.setter
    def width(self, value):
        """sets the value of width"""

        self._width = value

    @property
    def height(self):
        """"gets the attribute height"""

        return self._height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        
        self._heigth = value

    @property
    def x(self):
        """gets the attribute x"""

        return self._x

    @x.setter
    def x(self, value):
        """gets the value of x"""

        self._x = value

    @property
    def y(self):
        """gets the attribute y"""

        return self._y

    @y.setter
    def y(self, value):
        self._y = value
