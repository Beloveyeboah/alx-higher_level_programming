#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

if __name__ == "__main__":
    """This function prints of the command line"""

    import sys

    read = len(sys.argv) - 1
    if read == 0:
        print("0 arguments.")
    elif read == 1:
        print("1 argument: ")
    else:
        print("{} arguments:".format(read))
    for n in range(read):
        print("{}: {}".format(n + 1, sys.argv[n + 1]))
