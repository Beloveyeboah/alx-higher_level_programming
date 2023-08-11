#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

if __name__ == "__main__":
    import sys
    read = len(sys.argv) - 1
    if read == 0:
        print("0 arguments.")
    if read == 1:
        print("1 argument: ")
    else:
        print(f"{read} arguments:")
    for n in range(read):
        print("{}: {}".format(n+1, sys.argv[n + 1]))
