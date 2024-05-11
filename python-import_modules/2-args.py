#!/usr/bin/python3
from sys import argv


def print_it():
    count = len(argv) - 1  # Subtract 1 to exclude the script name

    if count == 0:
        print('0 arguments.')
    elif count == 1:
        print('{} argument:'.format(count))
    else:
        print('{} arguments:'.format(count))

    for i, arg in enumerate(argv[1:], start=1):
        print('{}: {}'.format(i, arg))


if __name__ == "__main__":
    print_it()
