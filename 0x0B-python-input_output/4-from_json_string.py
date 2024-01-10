#!/usr/bin/python3
"""defining from_json_string function"""
import json


def from_json_string(my_str):
    """convert JSON string into python object"""
    return json.loads(my_str)
