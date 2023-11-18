"""Solution to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24:
        return True
    elif 5 <= time <= 17:
        if coffee_needed:
            return True
        else:
            return False
    else:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c == 5:
        return 10
    elif a == b == c:
        return 5
    elif a != b and a != c:
        return 1
    else:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    number_of_smalls = 0
    while 5 <= ordered_amount and big_baskets > 0:
        ordered_amount -= 5
        big_baskets -= 1

    while 0 < ordered_amount and small_baskets > 0:
        ordered_amount -= 1
        small_baskets -= 1
        number_of_smalls += 1

    if ordered_amount == 0:
        return number_of_smalls
    else:
        return -1
