#!/usr/bin/python3
from sys import argv


def add_it():
    total = sum(int(arg) for arg in argv[1:])

    print(total)


if __name__ == '__main__':
    add_it()
