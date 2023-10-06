"""Tunnikontroll 2"""


def middle_value(arv1 :int, arv2: int, arv3: int):
    """Leiab keskmise väärtuse"""
    if min(arv1, arv2, arv3) == arv1 and max(arv1, arv2, arv3) == arv3:
        return arv2
    elif min(arv1, arv2, arv3) == arv2 and max(arv1, arv2, arv3) == arv1:
        return arv3
    elif min(arv1, arv2, arv3) == arv3 and max(arv1, arv2, arv3) == arv2:
        return arv1
    elif max(arv1, arv2, arv3) == arv1 and min(arv1, arv2, arv3) == arv3:
        return arv2
    elif max(arv1, arv2, arv3) == arv2 and min(arv1, arv2, arv3) == arv1:
        return arv3
    elif max(arv1, arv2, arv3) == arv3 and min(arv1, arv2, arv3) == arv2:
        return arv1
    else:
        return None


def lucky_guess(arv: int):
    """Arvamismäng"""
    fiveorsixinnumber = True

    if arv == 1 or arv == 3 or arv == 7:
        return True
    elif -6 <= arv <= 121 and arv % 13 == 0:
        return True
    else:
        for a in str(arv):
            if a == "5" or a == "6":
                fiveorsixinnumber = False
        if fiveorsixinnumber and arv < 0:
            return True
    return False


def without_end(s: str) -> str:
    """
    Given a string, return a version without the first and last char, so "Hello" yields "ell".

    The string length will be at least 2.

    without_end('Hello') → 'ell'
    without_end('java') → 'av'
    without_end('coding') → 'odin'

    :param s: String
    :return: String without first and last char.
    """
    if len(s) >= 2:
        s = s.strip(s[0])
        return s


def non_decreasing_list(nums: list) -> bool:
    """
    Given a list of numbers.

    If given list is a non-decreasing list, return True, otherwise False.
    Non-decreasing means every next element in the list must not be smaller than the previous one.

    non_decreasing_list([0, 1, 2, 3, 98]) => True
    non_decreasing_list([50, 49]) => False
    non_decreasing_list([12, 12]) => True

    :param nums:
    :return:
    """
    pass


def max_duplicate(nums: list) -> int | None:
    """
    Return the largest element which has at least one duplicate.

    If no element has duplicate element (an element with the same value), return None.

    max_duplicate([1, 2, 3]) => None
    max_duplicate([1, 2, 2]) => 2
    max_duplicate([1, 2, 2, 1, 1]) => 2

    :param nums: List of integers
    :return: Maximum element with duplicate. None if no duplicate found.
    """
    pass