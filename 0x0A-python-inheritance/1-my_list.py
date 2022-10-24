#!/usr/bin/python3
"""
    Module 1-my_list
    Contains Class MyList that inherits from class list
    inherits from list; has public method to print sorted
"""


class MyList(list):
    """
        Inherits from list
        Methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """ prints list of ints all sorted in ascending order """
        print(sorted(self))
