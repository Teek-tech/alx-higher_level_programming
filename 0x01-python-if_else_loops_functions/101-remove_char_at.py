#!/usr/bin/python3

def remove_char_at(str, n):
    str_copy = ""
    if len(str) == 0:
        return str
    for letter in range(len(str)):
        if letter != n:
            str_copy += str[letter]
    return str_copy
