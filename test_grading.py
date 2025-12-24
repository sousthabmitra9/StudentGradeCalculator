# tests/test_grading.py
from main import calculate_grade

def test_grading():
    assert calculate_grade(95) == 'A'
    assert calculate_grade(85) == 'B'
    assert calculate_grade(75) == 'C'
    assert calculate_grade(65) == 'D'
    assert calculate_grade(55) == 'E'
    assert calculate_grade(45) == 'F'
    print("All tests passed!")