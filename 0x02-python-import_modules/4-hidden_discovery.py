#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC
if __name__ == "__main__":

    import hidden_4

    hid = dir(hidden_4)
    for x in hid:
        if hid[:2] != "__":
            print(hid)
