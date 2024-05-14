#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        new_list = my_list.remove(my_list[idx])
    return my_list
