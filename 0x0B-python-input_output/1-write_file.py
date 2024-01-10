#!/usr/bin/python3
"""defining write file function"""


def write_file(filename="", text=""):
     """write 1-write_file.txt with utf-8"""
     with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

