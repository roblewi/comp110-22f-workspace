"""Working with dictionaries."""
__author__ = "730571332"


def invert(dict_to_flip: dict[str, str]) -> dict[str, str]:
    """Inverts a list."""
    new_dict: dict[str] = dict()
    new_key: str = ""
    new_value: str = ""
    for key in dict_to_flip:
        new_key = dict_to_flip[key]
        new_value = key
        if new_key in new_dict:
            raise KeyError("It is not possible to invert that list due to duplicate keys!")
        new_dict[new_key] = new_value
    return new_dict

xs = {'robert': 'periwinkle', 'you': 'periwinkle too? :)'}
print(invert(xs))

def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the most popular favorite color in a dictionary."""
    # Establishing i to start at the end of the list so that I can always return
    # the most popular entry starting at the beginning of the list.
    votes: int = 0
    popular_color: str = ""
    color_at_index: str = ""
    i: int = 0
    for key in names_and_colors:
        i = 0
        color_at_index = names_and_colors[key]
        for key in names_and_colors:
            if names_and_colors[key] == color_at_index:
                i += 1
        print(i)
        print(votes)
        if i > votes:
            votes = i
            popular_color = color_at_index
    if len(names_and_colors) == 0:
        return "null"
    return popular_color


def count(key_list: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = dict()
    for key in key_list:
        if not (key in count_dict):
            count_dict[key] = 1
        else:
            count_dict[key] += 1
    return count_dict

