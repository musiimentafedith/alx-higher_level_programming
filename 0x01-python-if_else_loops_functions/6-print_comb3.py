#!/usr/bin/python3
for i in range(0, 9):
    for k in range(1, 10):
        if k > i:
            if i == 8 and k == 9:
                print("{}{}".format(i, k))
            else:
                print("{}{}, ".format(i, k), end="")
