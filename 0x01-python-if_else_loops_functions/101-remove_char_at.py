#!/usr/bin/python3
def remove_char_at(str, p):
    if p < 0:
        return (str)
    return (str[:p] + str[p+1:])
