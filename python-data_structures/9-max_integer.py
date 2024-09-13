#!/usr/bin/python3
def max_integer(my_list=None):
    if my_list is None:
        my_list = []
    if len(my_list) == 0:
        return("None")
    x = my_list[0]
    for i in my_list:
        if i > x:
            x: int = 1
            return(x)
        