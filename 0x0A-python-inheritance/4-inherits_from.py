#!/usr/bin/python3

"""define direct or indirect inheritance"""

# CREATED: BELOVE YEBOAH ISAAC


def inherits_from(obj, a_class):
    """Write a function that returns True if
    the object is an instance of a class tha
    t inherited (directly or indirectly
    ) from the specified class ; otherwise False.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
