#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    replace = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return replace
    else:
        replace[idx] = element
        return replace
