#!/usr/bin/python3
def max_integer(my_list=[]):
    big1 = my_list[0]
    if len(my_list) > 0:
        for i in my_list:
            if i > big1:
                big1 = i
    return big1
