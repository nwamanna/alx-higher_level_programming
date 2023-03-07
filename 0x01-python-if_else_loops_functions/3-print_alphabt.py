#!/usr/bin/python3
# prints out all alphabets
for i in range(ord('a'), ord('z')+1):
	if (chr(i) == 'e') or (chr(i) == 'q'):
		continue
	print("{}".format(chr(i)), end="")
