#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    argc = len(argv)

    if argc != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    key = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
            }
    if argv[2] in key:
        num1 = int(argv[1])
        num2 = int(argv[3])
        key = key[argv[2]]
        ans = key(num1, num2)
        print("{:d} {:s} {:d} = {:d}".format(num1, argv[2], num2, ans))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
