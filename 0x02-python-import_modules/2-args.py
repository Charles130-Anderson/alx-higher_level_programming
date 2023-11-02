#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    length_argument = len(sys.argv)
    
    if length_argument == 1:
        print("{} arguments.".format(length_argument - 1))
    elif length_argument == 2:
        print("{} arguments.".format(length_argument - 1))
    else:
        print("{} arguments.".format(length_argument - 1))
    
    for y in range(1, length_argument):
        print("{}: {}.".format(y, sys.argv[y]))
