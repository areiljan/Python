"""KT3."""


def last_to_first(s):
    """
    Move last symbol to the beginning of the string.

    last_to_first("ab") => "ba"
    last_to_first("") => ""
    last_to_first("hello") => "ohell"
    """
    if s == "":
        return ""
    else:
        return s[-1] + s[:-1]


def only_one_pair(numbers: list) -> bool:
    """
    Whether the list only has one pair.

    Function returns True, if the list only has one pair (two elements have the same value).
    In other cases:
     there are no elements with the same value
     there are more than 2 elements with the same value
     there are several pairs
    returns False.

    only_one_pair([1, 2, 3]) => False
    only_one_pair([1]) => False
    only_one_pair([1, 2, 3, 1]) => True
    only_one_pair([1, 2, 1, 3, 1]) => False
    only_one_pair([1, 2, 1, 3, 1, 2]) => False
    """
    pair_count = 0
    for a in numbers:
        count = numbers.count(a)
        if count == 2:
            pair_count += 1

        if count >= 3:
            return False

    if pair_count == 2:
        return True
    else:
        return False

def swap_dict_keys_and_value_lists(d: dict) -> dict:
    """
    Swap keys and values in dict.

    Values are lists.
    Every element in this list should be a key,
    and current key will be a value for the new key.
    Values in the result are lists.

    Every list in input dict has at least 1 element.
    The order of the values in the result dict is not important.

    swap_dict_keys_and_value_lists({"a": ["b", "c"]}) => {"b": ["a"], "c": ["a"]}
    swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) => {2: [1, 4], 3: [1], 5: [4]}
    swap_dict_keys_and_value_lists({}) => {}
    swap_dict_keys_and_value_lists({1: [2]}) => {2: [1]}
    """
    swapped_dict = {}
    for keys, values in d.items():
        for value in values:
            if value not in swapped_dict:
                swapped_dict[value] = [keys]
            else:
                swapped_dict[value].append(keys)

    return swapped_dict



def substring(s: str, count: int) -> str:
    """
    Return first part of string with length of count.

    Function should be recursive, loops (for/while) are not allowed!
    count <= len(string)

    assert substring("hello", 2) == "he"
    assert substring("hi", 2) == "hi"
    assert substring("house", -1) == ""
    assert substring("house", 0) == ""

    :param s: input string.
    :param count: int, count <= len(string).
    :return: first count symbols from string.
    """
    if count <= 0:
        return ""
    if count >= len(s):
        return s
    return substring(s[:-1], count - 1)


if __name__ == '__main__':
    assert last_to_first("ab") == "ba"
    assert last_to_first("") == ""
    assert last_to_first("hello") == "ohell"

    assert only_one_pair([1, 2, 3]) is False
    assert only_one_pair([1]) is False
    assert only_one_pair([1, 2, 3, 1]) is True
    assert only_one_pair([1, 2, 1, 3, 1]) is False
    assert only_one_pair([1, 2, 1, 3, 1, 2]) is False

    assert swap_dict_keys_and_value_lists({"a": ["b", "c"]}) == {"b": ["a"], "c": ["a"]}
    assert swap_dict_keys_and_value_lists({1: [2, 3], 4: [2, 5]}) == {2: [1, 4], 3: [1], 5: [4]}  # or {2: [4, 1], 3: [1], 5: [4]}
    assert swap_dict_keys_and_value_lists({}) == {}
    assert swap_dict_keys_and_value_lists({1: [2]}) == {2: [1]}

    assert substring("hello", 2) == "he"
    assert substring("hello", -1) == ""
    assert substring("", 0) == ""
    assert substring("world", 5) == "world"

print(substring("hello", 2))
print(substring("hello", -1))
print(substring("", 0))
print(substring("world", 5))