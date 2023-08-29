#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC

def magic_calculation(a, b):
    ans = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            else:
                ans += a ** b / n
        except:
            ans = b = a
            break
    return ans

