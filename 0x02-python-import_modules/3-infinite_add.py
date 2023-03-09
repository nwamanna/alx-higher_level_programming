#!/usr/bin/python3
import sys
if __name__ == "__main__":
    array = sys.argv
    i = 1
    total = 0
    while i < len(array):
        total += int(array[i])
        i += 1
    print("{:d}".format(total))
