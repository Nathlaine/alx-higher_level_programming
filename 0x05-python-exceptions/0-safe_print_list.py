#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for k in range(x):
            print(my_list[k], end="")
        print()
        return x
    except IndexError:
        print()
        return k
