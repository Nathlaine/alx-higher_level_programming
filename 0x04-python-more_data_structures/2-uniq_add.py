#!/usr/bin/python3
def uniq_add(my_list=[]):

    new_list = []
    sum = 0
    for line in my_list:
        if line not in new_list:
            sum += line
            new_list.append(line)
    return sum
