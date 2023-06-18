#!/usr/bin/python3
for arg in range(100):
    if arg == 99:
        print("{}".format(arg))
    else:
        print("{:02d}".format(arg), end=", ")
