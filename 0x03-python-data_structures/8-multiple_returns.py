#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def multiple_returns(sentence):

    if sentence == "":
        return 0, None
    lenx = len(sentence)
    fis = sentence[0]
    return (lenx, fis)
