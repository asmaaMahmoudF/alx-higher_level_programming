#!/usr/bin/python3
import random
for i in range(100):
    if i == 99:
        print("{:02d} ".format(i), end="")
        break
    print("{:02d}, ".format(i), end="")
