"""Unit tests for the dictionary program."""
__author__ = "730571332"


from exercises.ex07.dictionary import invert, favorite_color, count

# Testing invert()


def test_invert_normal_dict() -> None:
    """Testing invert() with a normal list."""
    xs = {'robert': 'periwinkle', 'you': 'periwinkle too? :)'}
    assert invert(xs) == {'periwinkle': 'robert', 'periwinkle too? :)': 'you'}


def test_invert_long_dict() -> None:
    """Testing invert() with a long list!"""
    xs = {'a': 'B', 'c': 'D', 'e': 'F', 'g': 'H', 'i': 'J', 'k': 'L', 'm': 'N', 'o': 'P', 'q': 'R', 's': 'T', 'u': 'V', 'w': 'X', 'y': 'Z'}
    assert invert(xs) == {'B': 'a', 'D': 'c', 'F': 'e', 'H': 'g', 'J': 'i', 'L': 'k', 'N': 'm', 'P': 'o', 'R': 'q', 'T': 's', 'V': 'u', 'X': 'w', 'Z': 'y'}


def test_invert_blank_dict() -> None:
    """My favorite. So much simpler."""
    xs = {}
    assert invert(xs) == {}


# Testing favorite_color()


def test_favorite_color_clear_winner() -> None:
    """Testing favorite_color() with an unambiguous, clear winner."""
    xs = {'mark': 'blue', 'robert': 'periwinkle', 'jaime': 'periwinkle', 'zane': 'gray'}
    assert favorite_color(xs) == 'periwinkle'


def test_favorite_color_tie() -> None:
    """Testing favorite_color() in the situation of a tie."""
    xs = {'mark': 'blue', 'robert': 'periwinkle', 'jaime': 'periwinkle', 'zane': 'blue'}
    assert favorite_color(xs) == 'blue'


def test_favorite_color_blank() -> None:
    """My favorite again!"""
    xs = {}
    assert favorite_color(xs) == "null"


# Testing count()


def test_count_simple_list() -> None:
    xs = ['a', 'a', 'b', 'b', 'b']
    assert count(xs) == {'a': 2, 'b': 3}


def test_count_out_of_order_list() -> None:
    xs = ['banana', 'apple', 'pear', 'apple', 'banana', 'apple']
    assert count(xs) == {'banana': 2, 'apple': 3, 'pear': 1}


def test_count_empty_list() -> None:
    xs = []
    assert count(xs) == {}