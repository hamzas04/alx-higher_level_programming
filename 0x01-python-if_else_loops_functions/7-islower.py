#!/usr/bin/python3

"""
This module contains a function to check for lowercase characters.
"""

def islower(c):
    """
    Checks if a character is lowercase.

    Args:
        c (str): The character to check.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False


if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
