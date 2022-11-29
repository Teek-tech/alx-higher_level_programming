#!/usr/bin/python3

def print_last_digit(value):
    last_digit = 0
    if value >= 0:
        last_digit = value % 10
    else:
        last_digit = 10 - (value % 10)

    print('{:d}'.format(last_digit), end='')
    return last_digit
