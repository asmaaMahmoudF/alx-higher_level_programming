#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """read my_file_0.txt with utf-8"""
    with open('my_file_0', encoding='utf-8') as f:
        data = f.read()
        print(data)
