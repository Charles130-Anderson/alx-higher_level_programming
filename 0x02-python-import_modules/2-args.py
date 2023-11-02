if __name__ == "__main__":
    import sys

    arg = sys.argv
    length_argument = len(arg) - 1

    if length_argument == 1:
        print("{:d} argument.".format(length_argument))
    elif length_argument == 0:
        print("{:d} arguments.".format(length_argument))
    else:
        print("{:d} arguments:".format(length_argument))
        for y in range(1, len(arg)):
            print("{:d}: {}".format(y, arg[y]))
