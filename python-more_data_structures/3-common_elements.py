#!/usr/bin/python3
def common_elements(set_1, set_2):
    for i, j in zip(list(set_1), list(set_1)):
        if i == j:
            result = i
        return list(result)
