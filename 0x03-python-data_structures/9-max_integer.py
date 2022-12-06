#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        largest_no = my_list[0]
        for no in my_list:
            if no > largest_no:
                largest_no = no
        return largest_no
