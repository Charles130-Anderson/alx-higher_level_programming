#!/usr/bin/python3
for Anderson in range(97, 122 + 1):  # range of two numbers stored in Anderson
    if chr(Anderson) != "q" and chr(Anderson) != "e":  # Not equal to qand e
        print("{}" .format(chr(Anderson)), end="")
