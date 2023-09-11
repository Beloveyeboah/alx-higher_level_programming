#!/usr/bin/python3

# CREATED: BELOVE YEBOAH ISAAC

""" a class MyInt that inherits from int:"""


class MyInt(int):
    """revert operators  == and !="""

    def __eq__(self, value):
        """Orevert == opeartor to != behavior"""
        return self.real != value

    def __ne__(self, value):
        """revert != operator with == behavior"""
        return self.real == value
