#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col != row[-1]:
                print("{:d}".format(col),end = " ")
            else:
                ""
