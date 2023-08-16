#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def roman_to_int(roman_string):
    """converts into roman numbers"""

    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_digit = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }
    result = 0
    prev = 0

    for n in reversed(roman_string):
        value = roman_digit.get(n, 0)
        if value < prev:
            result -= value
        else:
            result += value
        prev = value
    return (result)
