"""Test cases for solution."""
from solution import students_study as study
from solution import lottery as lottery
from solution import fruit_order as fruit


def test_students_study_evening_false():
    """
    Evening no coffee.

    Expected result: True.
    """
    assert study(20, False) is True


def test_students_study_evening_true():
    """
    Evening coffee.

    Expected result: True.
    """
    assert study(20, True) is True


def test_students_study_morning_false():
    """
    Morning no coffee.

    Expected result: False.
    """
    assert study(10, False) is False


def test_students_study_morning_true():
    """
    Morning coffee.

    Expected result: True.
    """
    assert study(10, True) is True


def test_students_study_night_false():
    """
    Night no coffee.

    Expected result: False.
    """
    assert study(3, False) is False


def test_students_study_night_true():
    """
    Night coffee.

    Expected result: False.
    """
    assert study(3, True) is False


def test_students_study_evening_edge_false():
    """
    Edge case evening no coffee.

    Expected result: False.
    """
    assert study(18, False) is True


def test_students_study_evening_edge_true():
    """
    Edge case evening coffee.

    Expected result: True.
    """
    assert study(24, True) is True


def test_students_study_evening_edge_2_false():
    """
    Another edge case evening no coffee.

    Expected result: True.
    """
    assert study(24, False) is True


def test_students_study_evening_edge_2_true():
    """
    Another edge case evening coffee.

    Expected result: False.
    """
    assert study(18, True) is True


def test_students_study_morning_edge_false():
    """
    Edge case morning no coffee.

    Expected result: False.
    """
    assert study(5, False) is False


def test_students_study_morning_edge_true():
    """
    Edge case morning coffee.

    Expected result: True.
    """
    assert study(17, True) is True


def test_students_study_morning_edge_2_false():
    """
    Another edge case morning no coffee.

    Expected result: False.
    """
    assert study(17, False) is False


def test_students_study_morning_edge_2_true():
    """
    Another edge case morning no coffee.

    Expected result: True.
    """
    assert study(5, True) is True


def test_students_study_night_edge_false():
    """
    Edge case night no coffee.

    Expected result: False.
    """
    assert study(1, False) is False


def test_students_study_night_edge_true():
    """
    Edge case night coffee.

    Expected result: False.
    """
    assert study(1, True) is False


def test_students_study_night_edge_2_true():
    """
    Another edge case night coffee.

    Expected result: False.
    """
    assert study(4, True) is False


def test_students_study_night_edge_2_false():
    """
    Another edge case night no coffee.

    Expected result: False.
    """
    assert study(4, False) is False


def test_students_study_negative_time_true():
    """
    Time is negative, coffee.

    Expected result: False.
    """
    assert study(-1, True) is False


def test_students_study_negative_time_false():
    """
    Time is negative, no coffee.

    Expected result: False.
    """
    assert study(-1, False) is False


def test_students_study_big_time_true():
    """
    Time is larger than 24, coffee.

    Expected result: False.
    """
    assert study(30, True) is False


def test_students_study_big_time_false():
    """
    Time is larger than 24, no coffee.

    Expected result: False.
    """
    assert study(30, False) is False


def test_lottery_jackpot():
    """
    All integers are 5, jackpot.

    Expected result: 10.
    """
    assert lottery(5, 5, 5) == 10


def test_lottery_halfpot():
    """
    All integers are same, positive.

    Expected result: 5.
    """
    assert lottery(10, 10, 10) == 5


def test_lottery_halfpot_edge():
    """
    All integers are same, negative.

    Expected result: 5.
    """
    assert lottery(-10, -10, -10) == 5


def test_lottery_zeroes():
    """
    All integers are same, zeroes.

    Expected result: 5.
    """
    assert lottery(0, 0, 0) == 5


def test_lottery_ab_same_c_diff():
    """
    A and b are the same, c is different.

    Expected result: 0.
    """
    assert lottery(4, 4, 6) == 0


def test_lottery_ac_same_b_diff():
    """
    A and c are the same, b is different.

    Expected result: 0.
    """
    assert lottery(4, 7, 4) == 0


def test_lottery_bc_same_a_diff():
    """
    B and c are the same, a is different.

    Expected result: 1.
    """
    assert lottery(21, 2, 2) == 1


def test_lottery_all_diff():
    """
    B, c and a are all different.

    Expected result: 1.
    """
    assert lottery(21, 2, 24) == 1


def test_fruit_baskets_all_zeroes():
    """
    All values are zeroes.

    Expected result: 0.
    """
    assert fruit(0, 0, 0) == 0


def test_fruit_baskets_zero_big():
    """
    Not enough baskets, zero big baskets.

    Expected result: -1.
    """
    assert fruit(12, 0, 123) == -1


def test_fruit_baskets_zero_small():
    """
    Not enough baskets, zero small baskets.

    Expected result: -1.
    """
    assert fruit(0, 1, 1) == -1


def test_fruit_baskets_zero_small_zero_amount():
    """
    Enough baskets, zero small baskets.

    Expected result: 0.
    """
    assert fruit(0, 1, 0) == 0


def test_fruit_baskets_zero_big_zero_amount():
    """
    Enough baskets, zero big baskets and amount also zero.

    Expected result: 0.
    """
    assert fruit(1, 0, 0) == 0


def test_fruit_baskets_zero_both():
    """
    Not enough baskets, both baskets zero.

    Expected result: -1.
    """
    assert fruit(0, 0, 11) == -1


def test_fruit_baskets_zero_amount():
    """
    Enough baskets, both baskets are given, amount zero.

    Expected result: 0.
    """
    assert fruit(21, 123, 0) == 0


def test_fruit_baskets_exact_match_big():
    """
    Enough baskets, only big baskets are given, matches exactly.

    Expected result: 0.
    """
    assert fruit(0, 5, 25) == 0


def test_fruit_baskets_exact_match_small():
    """
    Enough baskets, only small baskets are given, matches exactly.

    Expected result: 21.
    """
    assert fruit(21, 0, 21) == 21


def test_fruit_baskets_big_but_not_enough():
    """
    Enough big baskets, but not enough total.

    Expected result: -1.
    """
    assert fruit(0, 2, 15) == -1


def test_fruit_baskets_small_but_not_enough():
    """
    Enough small baskets, but not enough total.

    Expected result: -1.
    """
    assert fruit(14, 0, 15) == -1


def test_fruit_baskets_only_big_more():
    """
    More than enough big baskets.

    Expected result: 0.
    """
    assert fruit(0, 15, 10) == 0


def test_fruit_baskets_only_small_more():
    """
    More than enough small baskets.

    Expected result: 12.
    """
    assert fruit(105, 0, 12) == 12


def test_fruit_baskets_big_exact():
    """
    Only big baskets, exact match.

    Expected result: 0.
    """
    assert fruit(0, 2, 10) == 0


def test_fruit_baskets_small_exact():
    """
    Both baskets, exact match.

    Expected result: 12.
    """
    assert fruit(12, 2, 22) == 12


def test_fruit_baskets_all_smalls_some_bigs():
    """
    Both baskets, exact match with smalls.

    Expected result: 4.
    """
    assert fruit(4, 2, 4) == 4


def test_fruit_baskets_some_smalls_all_bigs():
    """
    Both baskets, exact match with bigs.

    Expected result: 0.
    """
    assert fruit(12, 2, 10) == 0


def test_fruit_baskets_some_smalls_some_bigs():
    """
    Both baskets, exact match with some smalls and some bigs.

    Expected result: 1.
    """
    assert fruit(12, 2, 6) == 1


def test_fruit_baskets_not_enough():
    """
    Both baskets, not enough of those.

    Expected result: -1.
    """
    assert fruit(12, 2, 25) == -1


def test_fruit_baskets_enough_bigs_not_smalls():
    """
    Both baskets, enough bigs but not smalls.

    Expected result: -1.
    """
    assert fruit(3, 6, 14) == -1


def test_fruit_baskets_enough_bigs_not_smalls_large_numbers():
    """
    Both baskets, large numbers of all elements, there are enough bigs and not enough smalls.

    Expected result: -1.
    """
    assert fruit(2, 400000, 20128) == -1


def test_fruit_baskets_exact_match_large_numbers():
    """
    Both baskets are given, exact match, large numbers.

    Expected result: 1222.
    """
    assert fruit(1222, 4000, 21222) == 1222
