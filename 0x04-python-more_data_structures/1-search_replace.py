#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element with another element in a new list.

    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element to replace with.

    Returns:
        A new list with all occurrences of the search element replaced by the replace element.

    """
    # Create a new list to store the replaced elements
    new_list = []
    for item in my_list:
        # Check if the item is equal to the search element
        if item == search:
            # Replace the item with the replace element
            new_list.append(replace)
        else:
            # Keep the item unchanged
            new_list.append(item)
    return (new_list)
