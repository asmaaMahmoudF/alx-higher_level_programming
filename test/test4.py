#!/usr/bin/python3
for tens_digit in range(10):
	for ones_digit in range(tens_digit, 10):
		print("{:d}{:d}".format(tens_digit, ones_digit), ", " if tens_digit !=8 or ones_digit != 9 else "\n")
def islower(c):
	return ord('a') <= ord(c) >= ord('z')