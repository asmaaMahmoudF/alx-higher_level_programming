#!/usr/bin/python3
def islower(c):
    return ord('a') <= ord(c) <= ord('z')


def uppercase(str):

    for char in str:
        upper_case = ord(char) if not islower(char) else ord(char) - 32
        print("{:c}".format(upper_case), end='')
    print('')
