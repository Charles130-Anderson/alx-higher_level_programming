def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length

    for i in range(list_length):
        try:
            if not isinstance(my_list_1[i], (int, float)) or not isinstance(my_list_2[i], (int, float)):
                print("wrong type")
                result[i] = 0
            elif my_list_2[i] == 0:
                print("division by 0")
                result[i] = 0
            else:
                result[i] = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            break

    return result
