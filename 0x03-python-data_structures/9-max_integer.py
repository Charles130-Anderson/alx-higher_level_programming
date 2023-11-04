#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_number = my_list[0]
    for i in range(1, len(my_list)):
        if max_number < my_list[i]:
            max_number = my_list[i]  # Corrected variable name
    return max_number  # Moved this line out of the loop
