#!/usr/bin/python3

"""defines a base geometry"""

# CREATED: BELOVE YEBOAH ISAAC


class BaseGeometry:
    """Write an empty class BaseGeometry."""

    def area(self):
        """a class BaseGeome"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """args
        name
        value"""

        if type(value) is not int:
            raise TypeError("{}  must be an integer".format(name))
        if value <= 0:
            raise ValueError("{}  must be greater than 0".format(name))
