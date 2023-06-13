#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None
    temp = None
    for i in range(len(my_list) - 1):
        if temp == None or temp < my_list[i]:
            temp = my_list[i]
    return temp
