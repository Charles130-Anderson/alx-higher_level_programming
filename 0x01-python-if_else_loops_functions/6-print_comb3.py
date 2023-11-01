#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        # a represents first digit from left then b is the next digit
        if a >= b:
            continue
        elif a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            print("{}{}".format(a, b), end=", ")
            # a >=  b ,then ,it proceeds to else statement.
