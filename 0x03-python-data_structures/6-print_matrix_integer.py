#!/usr/bin/python3
def print_matrix_integer(n=[[]]):
    for col in n:
        for row in col:
            print("{}".format(row), end=" ")
        print()
