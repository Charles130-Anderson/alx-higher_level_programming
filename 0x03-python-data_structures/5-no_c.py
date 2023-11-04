def no_c(my_string):
    new_statement = my_string.translate({ord('c'): None, ord('C'): None})
    return new_statement
