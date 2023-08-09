#!/usr/bin/python3
# CREATED BY OSEI YEBOAH ISAAC

for i in range(0, 10):
    for r in range(i + 1, 10):
        if i == 8 and r == 9:
            print("{}{}".format(i, r))
        else:
            print("{}{}".format(i, r), end=", ")
