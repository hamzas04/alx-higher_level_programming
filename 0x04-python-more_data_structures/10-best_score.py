#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value in a dictionary.

    Args:
        a_dictionary: The input dictionary.

    Returns:
        The key with the biggest integer value, or None if no score is found.

    """
    if not a_dictionary:
        return (None)

    max_score = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score:
            max_score = value
            best_key = key

    return (best_key)
