#!/usr/bin/python3

"""
This program prints the ASCII alphabet in reverse order,
alternating lowercase and uppercase.
"""

for char_code in range(ord('z'), ord('a') - 1, -1):
    char = chr(char_code)
    if (char_code - ord('z')) % 2 == 0:
        char = char.upper()
    print("{}".format(char), end="")
