#!/usr/bin/python3
import sys
if __name__ == "__main__":
    array = sys.argv
    i = 1
    if len(array) - 1 == 0:
        print("0 arguments.")
    else:
        if len(array) - 1 == 1:
            print("{} argument:".format(len(array) - 1))
        else:
            print("{} arguments:".format(len(array) - 1))
        while i < len(array):
            print('{:d}: {}'.format(i, array[i]))
            i += 1
