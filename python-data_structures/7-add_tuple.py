#!.usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = [0, 0]

    for i in range(2):
        if i < len(tuple_a) and isinstance(tuple_a[i], int):
            result[i] += tuple_a[i]
        if i < len(tuple_b) and isinstance(tuple_b[i], int):
            result[i] += tuple_b[i]

    return tuple(result)