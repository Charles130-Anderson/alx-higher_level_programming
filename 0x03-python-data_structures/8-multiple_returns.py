#!/usr/bin/python3

def multiple_returns(sentence):
    total_length = len(sentence)
    if total_length == 0:
        return 0, None
    else:
        return total_length, sentence[0:1]
