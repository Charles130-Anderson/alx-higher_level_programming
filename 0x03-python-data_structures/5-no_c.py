def no_c(my_string):
 table = {ord('c'): None, ord('C'): None}
 return my_string.translate(table)

