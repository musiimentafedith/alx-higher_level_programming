#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_sum = 0
    for x in set(my_list):
        uni_sum += x
    return (uni_sum)
