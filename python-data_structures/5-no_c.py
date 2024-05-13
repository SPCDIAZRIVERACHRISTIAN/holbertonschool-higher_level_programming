#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if i == 'c':
            bye = my_string.maketrans("", "", "c")
            my_string = my_string.translate(bye)
        elif i == 'C':
            bye = my_string.maketrans("", "", "C")
            my_string = my_string.translate(bye)
    return my_string
