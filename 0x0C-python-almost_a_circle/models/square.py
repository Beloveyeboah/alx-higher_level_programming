#!/usr/bin/python3

""" defines Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """instances of square"""

    def __init__(self, size, x=0, y=0, id=None):
        """args:
        self.sze = size
        self.x = x
        """

        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """sets to prints strings"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """gets the attribute size"""

        return self.width

    @size.setter
    def size(self, value):
        """sets the attribute size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value
