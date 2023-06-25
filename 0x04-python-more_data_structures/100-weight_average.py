#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    average = 0
    div = 0
    for sub in my_list:
        average += sub[0] * sub[1]
        div += sub[1]
    return float(average / div)
