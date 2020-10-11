# binary_search.py
#
# A buggy version of Binary Search
#
# Usage:
#        python binary_search.py
#
# JDParker	Sept 2019


def binary_search(list_of_numbers: list, number: int) -> int:
    """Takes a list of numbers and a target value
       Returns the position of the target in the list"""

    # Set boundaries
    low = 0
    high = len(list_of_numbers) - 1

    # Check subarray list_of_numbers from low to high
    while (low <= high):
        mid = (low + high) // 2
        if number == list_of_numbers[mid]:
            # Found it!  Return index
            return mid
        elif number < list_of_numbers[mid]:
            high = mid 
        else:
            low = mid + 1

    # Not found 
    return -1


binary_search([1, 3, 4, 6, 8, 9, 11], 7)

binary_search([1, 3, 4, 6, 8, 9, 11], 0)

