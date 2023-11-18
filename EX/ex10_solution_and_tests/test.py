import pytest
from solution import students_study as study

def test_students_study_evening_false():
    assert study(18, False) == True

def test_students_study_evening_true():
    assert study(24, True) == True

def test_students_study_morning_false():
    assert study(5, False) == False

def test_students_study_morning_true():
    assert study(17, True) == True

def test_students_study_night_false():
    assert study(1, False) == False

def test_students_study_night_true():
    assert study(4, True) == False

def test_students_study_negative_time_true():
    assert study(-1, True) == False

def test_students_study_negative_time_false():
    assert study(-1, False) == False

def test_students_study_big_time_true():
    assert study(30, True) == False

def test_students_study_big_time_false():
    assert study(30, False) == False

