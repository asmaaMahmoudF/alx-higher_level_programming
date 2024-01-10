#!/usr/bin/python3
"""defining write file function"""


def write_file(filename="", text=""):
     """read my_file_0.txt with utf-8"""
     with open(filename, 'w') as f:
        f.write(text)
