#!/usr/bin/python3
"""defining to_json_string function"""
import json


def to_json_string(my_obj):
    """convert python object into JSON string"""
    return json.dumps(my_obj)
