#!/usr/bin/python3

"""defines a class Student that defines a student by:"""


class Student:
    """ a class of students"""

    def __init__(self, first_name, last_name, age):
        """ imitiate the args"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrive from init"""

        return self.__dict__
