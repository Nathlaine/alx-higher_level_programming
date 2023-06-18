#!/usr/bin/python3
for arg1 in range(10):
    for arg2 in range(arg1 + 1, 10):
        if arg1 == 8 and arg2 == 9:
            print("{}{}".format(arg1, arg2))
        else:
            print("{}{}".format(arg1, arg2), end=", ")
