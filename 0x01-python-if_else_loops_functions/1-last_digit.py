#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
elif number < 0:
    number2 = number * -1
    last = (number2 % 10) * -1
if last > 5:
    word = "and is greater than 5"
elif last == 0:
    word = "and is 0"
elif last < 6 and last != 0:
    word = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last, word))
