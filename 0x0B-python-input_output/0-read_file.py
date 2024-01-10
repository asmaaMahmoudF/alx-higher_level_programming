#!/usr/bin/python3
"""defining read_file function"""
def read_file(filename=""):
    """read my_file_0.txt with utf-8"""
    with open('my_file_0.txt', 'r', encoding='utf-8') as file:
        data = file.read()
        print(data)
