#!/usr/bin/python3


"""define a class base fro this project"""


class Base:
    """creates the bse class of the function"""

    __nb_objects = 0

    def __init__(self, id=None):
        """args - id"""

        if id != None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
