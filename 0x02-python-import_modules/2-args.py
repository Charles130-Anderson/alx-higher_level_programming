#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length_argument = len(sys.argv)

    if length_argument == 1:
        print("{:d} arguments.".format(length_argument - 1))
    elif length_argument == 2:
        print("{:d} argument.".format(length_argument - 1))
    else:
        print("{:d} arguments.".format(length_argument - 1))

    for y in range(1, length_argument):
        print("{:d}: {}".format(y, sys.argv[y]))
