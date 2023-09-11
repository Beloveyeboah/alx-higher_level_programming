#!/usr/bin/python3

"""define a class and inheritance"""


# CREATED: BELOVE YEBOAH ISAAC


def is_kind_of_class(obj, a_class):
    """function that returns true
    if the obj is a class
    or inherited from the sme type"""

    if isinstance(obj, a_class):
        return True
    return False
