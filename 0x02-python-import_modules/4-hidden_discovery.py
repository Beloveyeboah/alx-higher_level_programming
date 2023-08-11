#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC
if __name__ == "__main__":
    """prints hidden msg in hidden_4"""

    import hidden_4

    names = dir(hidden_4)
    for x in names:
        if x[:2] != "__":
            print(x)
