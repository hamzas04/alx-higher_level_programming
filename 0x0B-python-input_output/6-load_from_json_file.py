#!/usr/bin/python3
"""This module defines a function 'load_from_json_file'"""
import json

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        json_data = file.read()
        obj = json.loads(json_data)
        return obj
