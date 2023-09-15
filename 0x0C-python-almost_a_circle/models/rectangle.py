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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the attribute width"""

        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""

        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """"gets the attribute height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""

        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        
        self.__heigth = value

    @property
    def x(self):
        """gets the attribute x"""

        return self.__x

    @x.setter
    def x(self, value):
        """gets the value of x"""

        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """gets the attribute y"""

        return self.__y

    @y.setter
    def y(self, value):
        """sets the value for y"""

        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
