#!/usr/bin/python3
"""defining save_to_json_file function"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
