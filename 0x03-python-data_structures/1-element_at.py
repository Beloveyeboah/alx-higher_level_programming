#!/usr/bin/python3

# CREATED BY OSEI YEBOAH ISAAC
def element_at(my_list, idx):
    """functiom returns index of num"""
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return (my_list[idx])
