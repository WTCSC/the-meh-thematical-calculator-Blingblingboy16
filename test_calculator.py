import pytest
from calculator import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(6, 7) == 13

def test_add_negative_numbers():
    assert add(-4, -5) == -9

def test_subtract_positive_numbers():
    assert subtract(3, 6) == -3

def test_subtract_negative_numbers():
    assert subtract(-4, -2) == -2

def test_multiply_positive_numbers():
    assert multiply(8, 1) == 8

def test_multiply_negative_numbers():
    assert multiply(-3, -3) == 9

def test_divide_positive_numbers():
    assert divide(9, 3) == 3

def test_divide_by_one():
    assert divide(5, 1) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


