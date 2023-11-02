#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length_arguments = len(sys.argv)
    total = 0

    if length_arguments == 1:
        total = 0
    else:
        for y in range(1, length_arguments):
            total += int(sys.argv[y])

    print("{:d}".format(total))
