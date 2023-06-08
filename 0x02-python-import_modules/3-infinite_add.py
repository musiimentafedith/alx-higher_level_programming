#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    _len = len(sys.argv) - 1
    if _len == 0:
        print(0)
    else:
        argsum = 0
        for i in range(1, _len + 1):
            argsum += int(sys.argv[i])
        print(argsum)
