#!/usr/bin/python3

def multiple_returns(sentence):
    convert_sentence = list(sentence)
    char_length = len(convert_sentence)
    if char_length == 0:
        first_char = None
    else:
        first_char = convert_sentence[0]
    return (char_length, first_char)
