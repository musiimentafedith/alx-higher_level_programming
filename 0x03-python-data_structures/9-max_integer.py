#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    temp = 0
    for i in range(len(my_list) - 1):
        if temp == 0 or temp < my_list[i]:
            temp = my_list[i]
    return temp
