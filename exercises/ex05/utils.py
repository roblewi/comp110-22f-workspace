"""fill"""
__author__ = "730571332"

def only_evens(int_list: list[int]) -> list[int]:
    """Returns only even numbers in a list."""
    only_evens_list = []
    i = 0
    while i < len(int_list):
        """Checking for evens."""
        if i % 2 == 0:
            only_evens_list.append(int_list[i])
        """Avoiding certain doom."""
        i += 1
    return only_evens_list


def concat(int_list_one: list[int], int_list_two: list[int]) -> list[int]:
    """Will concatenate the elements of the two lists."""
    concat_list = []
    i = 0
    j = 0
    while i < len(int_list_one):
        """Iterating through the first list."""
        concat_list.append(int_list_one[i])
        """Avoiding division by zero."""
        i += 1
    while j < len(int_list_two):
        """Iterating through the second list."""
        concat_list.append(int_list_two[j])
        """Avoiding World War III."""
        j += 1
    return concat_list


def sub(int_list: list[int]) -> list[int]:
    """Will return the elements of the list between index 0 and -1."""
    sub_return = []
    i = 1
    while i < (len(int_list) - 1):
        """Starting at index 1, append every following element except the last."""
        sub_return.append(int_list[i])
        """Avoiding the collapse of the space-time continuum."""
        i += 1
    return sub_return