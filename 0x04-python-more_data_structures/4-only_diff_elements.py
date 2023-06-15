#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A set containing the elements that are present in only one of the sets.

    """
    # Find the symmetric difference of set_1 and set_2
    diff_elements_set = set_1.symmetric_difference(set_2)

    return (diff_elements_set)
