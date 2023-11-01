#!/usr/bin/python3
for numbers_ascending in range(0, 97 + 3):
    if numbers_ascending == 99:
        print("{}".format(numbers_ascending))
    else:
        print("{:02}".format(numbers_ascending), end=",")
    #  Ascending order formating with 02 ,seperated by a comma,in a range.
