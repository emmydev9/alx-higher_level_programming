#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return my_list
    elif idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        new_list = my_list
        my_list.pop(idx)

    return new_list
