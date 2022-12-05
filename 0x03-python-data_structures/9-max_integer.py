#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_number = None
        for number in my_list:
            if max_number is None or max_number < number:
                max_number = number
        return max_number
