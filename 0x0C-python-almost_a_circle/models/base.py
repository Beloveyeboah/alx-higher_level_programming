#!/usr/bin/python3


"""define a class base fro this project"""

import json
import os


class Base:
    """creates the bse class of the function"""

    __nb_objects = 0

    def __init__(self, id=None):
        """args - id"""

        if id is not None:
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

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json into a file"""

        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_dict = [conv.to_dictionary() for conv in list_objs]
                f.write(Base.to_json_string(json_dict))

    @staticmethod
    def from_json_string(json_string):
        """reads from a json. file"""

        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        file_name = cls.__name__ + ".json"
        if not os.path.exists(file_name):
            return "[]"
        with open(file_name, "r") as f:
            list_of_instances = []
            list_dictionaries = []
            
            m_list = f.read()
            list_dictionaries = cls.from_json_string(m_list)
            for dictionary in list_dictionaries:
                list_of_instances.append(cls.create(**dictionary))
        return list_of_instances


