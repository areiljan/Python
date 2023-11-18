import pytest
from solution import students_study as study
from solution import lottery as lottery
from solution import fruit_order as fruit

def test_students_study_evening_false():
    assert study(20, False) == True

def test_students_study_evening_true():
    assert study(20, True) == True

def test_students_study_morning_false():
    assert study(10, False) == False

def test_students_study_morning_true():
    assert study(10, True) == True

def test_students_study_night_false():
    assert study(3, False) == False

def test_students_study_night_true():
    assert study(3, True) == False

def test_students_study_evening_edge_false():
    assert study(18, False) == True

def test_students_study_evening_edge_true():
    assert study(24, True) == True

def test_students_study_evening_edge_2_false():
    assert study(24, False) == True

def test_students_study_evening_edge_2_true():
    assert study(18, True) == True

def test_students_study_morning_edge_false():
    assert study(5, False) == False

def test_students_study_morning_edge_true():
    assert study(17, True) == True

def test_students_study_morning_edge_2_false():
    assert study(17, False) == False

def test_students_study_morning_edge_2_true():
    assert study(5, True) == True

def test_students_study_night_edge_false():
    assert study(1, False) == False

def test_students_study_night_edge_true():
    assert study(1, True) == False

def test_students_study_night_edge_2_true():
    assert study(4, True) == False

def test_students_study_night_edge_2_false():
    assert study(4, False) == False

def test_students_study_negative_time_true():
    assert study(-1, True) == False

def test_students_study_negative_time_false():
    assert study(-1, False) == False

def test_students_study_big_time_true():
    assert study(30, True) == False

def test_students_study_big_time_false():
    assert study(30, False) == False

def test_lottery_jackpot():
    assert lottery(5, 5, 5) == 10

def test_lottery_halfpot():
    assert lottery(10, 10, 10) == 5

def test_lottery_halfpot_edge():
    assert lottery(-10, -10, -10) == 5

def test_lottery_zeroes():
    assert lottery(0, 0, 0) == 5

def test_lottery_ab_same_c_diff():
    assert lottery(4, 4, 6) == 0

def test_lottery_ac_same_b_diff():
    assert lottery(4, 7, 4) == 0

def test_lottery_bc_same_a_diff():
    assert lottery(21, 2, 2) == 1

def test_lottery_ab_same_c_diff():
    assert lottery(4, 4, 6) == 0

def test_lottery_all_diff():
    assert lottery(21, 2, 24) == 1

def test_fruit_baskets_all_zeroes():
    assert fruit(0, 0, 0) == 0

def test_fruit_baskets_zero_big():
    assert fruit(12, 0, 123) == -1

def test_fruit_baskets_zero_small():
    assert fruit(0, 1, 1) == -1

def test_fruit_baskets_zero_small_zero_amount():
    assert fruit(0, 1, 0) == 0

def test_fruit_baskets_zero_big_zero_amount():
    assert fruit(1, 0, 0) == 0

def test_fruit_baskets_zero_both():
    assert fruit(0, 0, 11) == -1

def test_fruit_baskets_zero_amount():
    assert fruit(21, 123, 0) == 0

def test_fruit_baskets_exact_match_big():
    assert fruit(0, 5, 25) == 0

def test_fruit_baskets_exact_match_small():
    assert fruit(21, 0, 21) == 21

def test_fruit_baskets_big_but_not_enough():
    assert fruit(0, 2, 15) == -1

def test_fruit_baskets_small_but_not_enough():
    assert fruit(14, 0, 15) == -1

def test_fruit_baskets_only_big_more():
    assert fruit(0, 15, 10) == 0

def test_fruit_baskets_only_small_more():
    assert fruit(105, 0, 12) == 12

def test_fruit_baskets_big_exact():
    assert fruit(0, 2, 10) == 0

def test_fruit_baskets_small_exact():
    assert fruit(12, 2, 22) == 12

def test_fruit_baskets_all_smalls_some_bigs():
    assert fruit(4, 2, 4) == 4

def test_fruit_baskets_some_smalls_all_bigs():
    assert fruit(12, 2, 10) == 0

def test_fruit_baskets_some_smalls_some_bigs():
    assert fruit(12, 2, 6) == 1

def test_fruit_baskets_not_enough():
    assert fruit(12, 2, 25) == -1

def test_fruit_baskets_enough_bigs_not_smalls():
    assert fruit(3, 2, 14) == -1

def test_fruit_baskets_enough_bigs_not_smalls_large_number():
    assert fruit(3, 14, 144) == -1









