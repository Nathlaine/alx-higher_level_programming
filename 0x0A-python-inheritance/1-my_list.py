#!/usr/bin/python3
"""This project inherits from the list class"""


class MyList(list):
    """A class inherits from list"""
    def print_sorted(self):
        """print a sorted list"""
        print(sorted(self))
