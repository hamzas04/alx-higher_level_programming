#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list, considering each integer only once.

    Args:
        my_list: The list of integers.

    Returns:
        The sum of all unique integers in the list.

    """
    # Create an empty set to store unique integers
    unique_integers = set()

    # Iterate through the list and add unique integers to the set
    for num in my_list:
        unique_integers.add(num)

    # Calculate the sum of unique integers
    sum_unique = sum(unique_integers)

    return (sum_unique)
