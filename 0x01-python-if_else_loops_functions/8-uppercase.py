#!/usr/bin/python3

"""
This module contains a function to print a string in uppercase.
"""

def uppercase(string):
    """
    Prints a string in uppercase.

    Args:
        string (str): The string to print.

    Returns:
        None
    """
    result = ""
    for char in string:
        if ord(char) >= 97 and ord(char) <= 122:
            char = chr(ord(char) - 32)
        result += char
    print("{}".format(result), end="\n")
