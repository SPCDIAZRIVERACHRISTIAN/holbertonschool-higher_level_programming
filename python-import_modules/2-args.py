#!/usr/bin/python3
from sys import argv

def print_it():
    count = len(argv)
    
    if count == 0:
        print('0 arguments')
    elif count == 1:
        print('{} argument'.format(count))
    else:
        print('{} arguments'.format(count))

    for i in argv:
        if argv(i) > 1:
            print('{}: {}'.format(i, argv))

if __name__ == "__main__":
    main()
