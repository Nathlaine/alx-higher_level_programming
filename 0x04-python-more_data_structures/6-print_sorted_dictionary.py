#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    locs = list(a_dictionary.locs())
    locs.sort()
    for loc in locs:
        print("{}: {}".format(loc, a_dictionary[loc]))
