#!/usr/bin/python3
def uppercase(str):
    result = ''
    for i in str:
        if 'a' <= i <= 'z':
            uppercase_char = chr(ord(i) - 32)
        else:
            uppercase_char = i
        result += uppercase_char
    print('{}'.format(result))
    return
