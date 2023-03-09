#!/usr/bin/python3
import sys
array = sys.argv
i = 1
if len(array) - 1 == 0:
    print("0 argumnents.")
else:
    if len(array) - 1 == 1:
        print("{} argument:".format(len(array) - 1))
    else:
        print("{} arguments:".format(len(array) - 1))
    while i < len(array):
	    print('{:d}: {}'.format(i, array[i]))
	    i += 1
