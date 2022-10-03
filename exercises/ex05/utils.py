"""A plethora of fun functions that deal with lists."""
__author__ = "730571332"


def only_evens(int_list: list[int]) -> list[int]:
    """Returns only even numbers in a list."""
    only_evens_list = []
    i = 0
    while i < len(int_list):
        """Checking for evens."""
        if int_list[i] % 2 == 0:
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


def sub(int_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Will return the elements of the list between index 0 and -1."""
    sub_return = []
    """Making sure user is not trying to break my program."""
    a = (len(int_list) == 0)
    b = (start_index > len(int_list))
    c = (end_index == 0)
    if a or b or c:
        return []

    """Correcting for negative start_index values."""
    while start_index < 0:
        start_index += 1
    
    """Correcting for out-of-range end_list values."""
    while end_index > len(int_list):
        end_index -= 1

    while start_index < end_index:
        """Starting at index 1, append every following element except the last."""
        sub_return.append(int_list[start_index])
        """Avoiding the collapse of the space-time continuum."""
        start_index += 1
    return sub_return