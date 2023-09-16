#!/usr/bin/python3


"""define a class base fro this project"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """initialize a json to strings"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for item in list_dictionaries:
            if not isinstance(item, dict):
                raise TypeError("Each item in list must be a dictionary")
        else:
            return json.dumps(list_dictionaries)
