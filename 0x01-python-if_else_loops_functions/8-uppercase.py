#!/usr/bin/python3

def to_uper(letter):
    if ord(letter) >= 97 and ord(letter) <= 122:
        return (ord(letter) - 32)
    else:
        return ord(letter)


def uppercase(str):
    new_letter = ""
    for letter in str:
        new_letter += "%c" % to_uper(letter)
    print("{:s}".format(new_letter))
