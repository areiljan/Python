import pytest
from solution import students_study as study

def test_students_study_evening_false():
    assert study(19, False) == True

def test_students_study_evening_true():
    assert study(19, True) == True

def test_students_study_morning_false():
    assert study(10, False) == False

def test_students_study_morning_true():
    assert study(10, True) == True

def test_students_study_night_false():
    assert study(3, False) == False

def test_students_study_night_true():
    assert study(3, True) == False

