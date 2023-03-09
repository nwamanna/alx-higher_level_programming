#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(sys.argv) == 4:
        array = sys.argv
        a = int(array[1])
        b = int(array[3])
        operator = array[2]
        if operator == '+':
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, add(a, b)))
        elif operator == '-':
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print('{:d} {} {:d} = {:d}'.format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    sys.exit(0)
