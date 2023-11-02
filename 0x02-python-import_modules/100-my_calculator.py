#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    User_input = argv[1:]
    Count = len(User_input)
    operator = ["+", "-", "*", "/"]

    if Count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif argv[2] not in operator:
        print("Available operators: +, -, * and /")
    else:
        if argv[2] == operator[0]:
            a = int(User_input[0])
            b = int(User_input[2])
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == operator[1]:
            a = int(User_input[0])
            b = int(User_input[2])
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == operator[2]:
            a = int(User_input[0])
            b = int(User_input[2])
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            a = int(User_input[0])
            b = int(User_input[2])
            print("{} / {} = {}".format(a, b, div(a, b)))
