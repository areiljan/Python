"""Solution to be tested."""
def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if 18 <= time <= 24:
        return True
    elif  5 <= time <= 17:
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
    small_capacity = 1
    big_capacity = 5
    max_big_baskets = ordered_amount // big_capacity
    actual_big_baskets = min(max_big_baskets, big_baskets)
    remaining_amount = ordered_amount - (actual_big_baskets * big_capacity)
    required_small_baskets = remaining_amount // small_capacity
    total_baskets = actual_big_baskets + required_small_baskets
    if total_baskets * small_capacity == ordered_amount:
        return required_small_baskets
    else:
        return -1