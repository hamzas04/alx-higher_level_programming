#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds a key/value pair in a dictionary.

    Args:
        a_dictionary: The input dictionary.
        key: The key to replace or add.
        value: The value to set for the key.

    Returns:
        None

    """
    if isinstance(a_dictionary, dict):
        a_dictionary[key] = value
    return (a_dictionary)
