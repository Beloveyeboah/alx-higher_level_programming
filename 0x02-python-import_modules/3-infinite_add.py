#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC
if __name__ == "__main__":

    import sys

    count = 0
    for n in range(len(sys.argv) - 1):
        count = count + int(sys.argv[n + 1])
    print("{}".format(count))
