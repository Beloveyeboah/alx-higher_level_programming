#!/usr/bin/python3

# CREAted by osei yeboah

"""print program that prints the ASCII alphabet"""

for i in range(97, 123):
    if chr(i) != "q" and chr(i) != "e":
        print("{}".format(chr(i)), end="")
