#!/usr/bin/python3
"""defining save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Save an object to json file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """load_from_json_file"""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
