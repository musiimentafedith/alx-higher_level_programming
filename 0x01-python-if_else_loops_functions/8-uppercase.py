#!/usr/bin/python3
def uppercase(str):
    for k in str:
        if ord(k) > 96:
            k = chr(ord(k) - 32)
        print("{}".format(k), end="")
    print("")
