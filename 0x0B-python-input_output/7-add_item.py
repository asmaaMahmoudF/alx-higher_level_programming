#!/usr/bin/python3
"""add item"""


import json
import sys
import os.path
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    old_data = load_from_json_file(filename)
except FileNotFoundError:
    old_data = []
old_data.extend(sys.argv[1:])
save_to_json_file(old_data, filename)
