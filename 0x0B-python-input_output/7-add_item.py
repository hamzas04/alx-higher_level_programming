#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file
"""

import json
import sys
from os.path import exists
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = 'add_item.json'

# Check if the file exists
if exists(filename):
    # Load existing data from file
    my_list = load_from_json_file(filename)
else:
    # Create an empty list if the file doesn't exist
    my_list = []

# Add arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(my_list, filename)
