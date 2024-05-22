#!/usr/bin/python3
"""A class inherited from list."""


class MyList(list):
    """Subclass inherited from list."""
    def __init__(self):
        """This function initializes object."""
        super().__init__()

    def print_sorted(self):
        """This function prints the list in sorted order."""
        print(sorted(self))
