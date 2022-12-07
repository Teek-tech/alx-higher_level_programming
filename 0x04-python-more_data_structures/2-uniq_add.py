#!/usr/bin/python3

def uniq_add(my_list=[]):
    if my_list is not None:
        result = 0
        for f in sorted(set(my_list)):
            result += f
        return result
