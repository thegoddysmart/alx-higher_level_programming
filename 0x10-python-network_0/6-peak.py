#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak value.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # If the middle element is greater than the next element, a peak may exist on the left side
            high = mid
        else:
            # If the middle element is less than or equal to the next element, a peak may exist on the right side
            low = mid + 1

    return list_of_integers[low]
