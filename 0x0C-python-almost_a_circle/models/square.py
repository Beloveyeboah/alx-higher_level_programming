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



