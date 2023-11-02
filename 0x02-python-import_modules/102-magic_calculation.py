#!/usr/bin/python3
import dis


def magic_calculation(a, b):
    from magic_calculation import add, sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(a, b)
            return c
    else:
        return sub(a, b)


dis.dis(magic_calculation)
