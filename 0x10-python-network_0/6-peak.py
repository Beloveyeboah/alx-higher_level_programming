#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ algorithm must have the lowest complexity """

    length = len(list_of_integers)
    mid_e = length
    mid = length // 2

    if length == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < length - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return list_of_integers[mid]
