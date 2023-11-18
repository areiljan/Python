"""Test cases for solution."""
from solution import students_study as study
from solution import lottery as lottery
from solution import fruit_order as fruit


def test_students_study_evening_false():
    """
        Evening no coffee.

        Expected result: True.
    """
    assert study(20, False) == True


def test_students_study_evening_true():
    """
            Evening coffee.

            Expected result: True.
    """
    assert study(20, True) == True


def test_students_study_morning_false():
    """
            Morning no coffee.

            Expected result: False.
    """
    assert study(10, False) == False


def test_students_study_morning_true():
    """
            Morning coffee.

            Expected result: True.
    """
    assert study(10, True) == True


def test_students_study_night_false():
    """
            Night no coffee.

            Expected result: False.
    """
    assert study(3, False) == False


def test_students_study_night_true():
    """
            Night coffee.

            Expected result: False.
    """
    assert study(3, True) == False


def test_students_study_evening_edge_false():
    """
            edge case evening no coffee.

            Expected result: False.
    """
    assert study(18, False) == True


def test_students_study_evening_edge_true():
    """
            edge case evening coffee.

            Expected result: True.
    """
    assert study(24, True) == True


def test_students_study_evening_edge_2_false():
    """
            another edge case evening no coffee.

            Expected result: True.
    """
    assert study(24, False) == True


def test_students_study_evening_edge_2_true():
    """
            another edge case evening coffee.

            Expected result: False.
    """
    assert study(18, True) == True


def test_students_study_morning_edge_false():
    """
            edge case morning no coffee.

            Expected result: False.
    """
    assert study(5, False) == False


def test_students_study_morning_edge_true():
    """
            edge case morning coffee.

            Expected result: True.
    """
    assert study(17, True) == True


def test_students_study_morning_edge_2_false():
    """
            another edge case morning no coffee.

            Expected result: False.
    """
    assert study(17, False) == False


def test_students_study_morning_edge_2_true():
    """
            another edge case morning no coffee.

            Expected result: True.
    """
    assert study(5, True) == True


def test_students_study_night_edge_false():
    """
            edge case night no coffee.

            Expected result: False.
    """
    assert study(1, False) == False


def test_students_study_night_edge_true():
    """
            edge case night coffee.

            Expected result: False.
    """
    assert study(1, True) == False


def test_students_study_night_edge_2_true():
    """
            another edge case night coffee.

            Expected result: False.
    """
    assert study(4, True) == False


def test_students_study_night_edge_2_false():
    """
            another edge case night no coffee.

            Expected result: False.
    """
    assert study(4, False) == False


def test_students_study_negative_time_true():
    """
            time is negative, coffee.

            Expected result: False.
    """
    assert study(-1, True) == False


def test_students_study_negative_time_false():
    """
            time is negative, no coffee.

            Expected result: False.
    """
    assert study(-1, False) == False


def test_students_study_big_time_true():
    """
            time is larger than 24, coffee.

            Expected result: False.
    """
    assert study(30, True) == False


def test_students_study_big_time_false():
    """
            time is larger than 24, no coffee.

            Expected result: False.
    """
    assert study(30, False) == False


def test_lottery_jackpot():
    """
            all integers are 5, jackpot.

            Expected result: 10.
    """
    assert lottery(5, 5, 5) == 10


def test_lottery_halfpot():
    """
            all integers are same, positive.

            Expected result: 5.
    """
    assert lottery(10, 10, 10) == 5


def test_lottery_halfpot_edge():
    """
            all integers are same, negative.

            Expected result: 5.
    """
    assert lottery(-10, -10, -10) == 5


def test_lottery_zeroes():
    """
            all integers are same, zeroes.

            Expected result: 5.
    """
    assert lottery(0, 0, 0) == 5


def test_lottery_ab_same_c_diff():
    """
            a and b are the same, c is different.

            Expected result: 0.
    """
    assert lottery(4, 4, 6) == 0


def test_lottery_ac_same_b_diff():
    """
            a and c are the same, b is different.

            Expected result: 0.
    """
    assert lottery(4, 7, 4) == 0


def test_lottery_bc_same_a_diff():
    """
            b and c are the same, a is different.

            Expected result: 1.
    """
    assert lottery(21, 2, 2) == 1


def test_lottery_all_diff():
    """
            b, c and a are all different.

            Expected result: 1.
    """
    assert lottery(21, 2, 24) == 1


def test_fruit_baskets_all_zeroes():
    """
            all values are zeroes.

            Expected result: 0.
    """
    assert fruit(0, 0, 0) == 0


def test_fruit_baskets_zero_big():
    """
            not enough baskets, zero big baskets.

            Expected result: -1.
    """
    assert fruit(12, 0, 123) == -1


def test_fruit_baskets_zero_small():
    """
            not enough baskets, zero small baskets.

            Expected result: -1.
    """
    assert fruit(0, 1, 1) == -1


def test_fruit_baskets_zero_small_zero_amount():
    """
            enough baskets, zero small baskets.

            Expected result: 0.
    """
    assert fruit(0, 1, 0) == 0


def test_fruit_baskets_zero_big_zero_amount():
    """
            enough baskets, zero big baskets and amount also zero.

            Expected result: 0.
    """
    assert fruit(1, 0, 0) == 0


def test_fruit_baskets_zero_both():
    """
            not enough baskets, both baskets zero.

            Expected result: -1.
    """
    assert fruit(0, 0, 11) == -1


def test_fruit_baskets_zero_amount():
    """
            enough baskets, both baskets are given, amount zero.

            Expected result: 0.
    """
    assert fruit(21, 123, 0) == 0


def test_fruit_baskets_exact_match_big():
    """
            enough baskets, only big baskets are given, matches exactly.

            Expected result: 0.
    """
    assert fruit(0, 5, 25) == 0


def test_fruit_baskets_exact_match_small():
    """
            enough baskets, only small baskets are given, matches exactly.

            Expected result: 21.
    """
    assert fruit(21, 0, 21) == 21


def test_fruit_baskets_big_but_not_enough():
    """
            enough big baskets, but not enough total.

            Expected result: -1.
    """
    assert fruit(0, 2, 15) == -1


def test_fruit_baskets_small_but_not_enough():
    """
            enough small baskets, but not enough total.

            Expected result: -1.
    """
    assert fruit(14, 0, 15) == -1


def test_fruit_baskets_only_big_more():
    """
            more than enough big baskets.

            Expected result: 0.
    """
    assert fruit(0, 15, 10) == 0


def test_fruit_baskets_only_small_more():
    """
            more than enough small baskets.

            Expected result: 12.
    """
    assert fruit(105, 0, 12) == 12


def test_fruit_baskets_big_exact():
    """
            only big baskets, exact match.

            Expected result: 0.
    """
    assert fruit(0, 2, 10) == 0


def test_fruit_baskets_small_exact():
    """
            both baskets, exact match.

            Expected result: 12.
    """
    assert fruit(12, 2, 22) == 12


def test_fruit_baskets_all_smalls_some_bigs():
    """
            both baskets, exact match with smalls.

            Expected result: 4.
    """
    assert fruit(4, 2, 4) == 4


def test_fruit_baskets_some_smalls_all_bigs():
    """
            both baskets, exact match with bigs.

            Expected result: 0.
    """
    assert fruit(12, 2, 10) == 0


def test_fruit_baskets_some_smalls_some_bigs():
    """
            both baskets, exact match with some smalls and some bigs.

            Expected result: 1.
    """
    assert fruit(12, 2, 6) == 1


def test_fruit_baskets_not_enough():
    """
            both baskets, not enough of those.

            Expected result: -1.
    """
    assert fruit(12, 2, 25) == -1


def test_fruit_baskets_enough_bigs_not_smalls():
    """
            both baskets, enough bigs but not smalls.

            Expected result: -1.
    """
    assert fruit(3, 6, 14) == -1


def test_fruit_baskets_enough_bigs_not_smalls_large_numbers():
    """
            both baskets, large numbers of all elements, there are enough bigs and not enough smalls.

            Expected result: -1.
    """
    assert fruit(2, 400000, 20128) == -1


def test_fruit_baskets_exact_match_large_numbers():
    """
            both baskets are given, exact match, large numbers.

            Expected result: 1222.
    """
    assert fruit(1222, 4000, 21222) == 1222


