#!/usr/bin/python3

def uppercase(str):
    upcount = ""
    for i in str:
        if  ord(i) >= 97 and ord(i) <= 122:
            convert = chr(ord(i) - 32)
            upcount += convert
        else:
            upcount += i
    print("{}".format(upcount))

my = "oNE of the  BEST SCHools"
uppercase(my)
