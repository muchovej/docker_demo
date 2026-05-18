import pytest
from src.add import add

def test_addition_happy_path():
    assert add(2,3) == 5

def test_addition_float():
    assert add(2.0, 3.0) == 5

def test_negative_value():
    assert add(-2, 3) == 1

def test_two_negs():
    assert add(-2,-3) == -5

@pytest.mark.parametrize(
    "input1, input2, input3, expected",
    [(2,3,5,10), (2.0,3.0, 5,10), (-2,3,1), (-2,-3,-5), (10, 2, 12)],
)
def test_add(input1, input2, input3, expected):
    assert add(input1, input2, input3) == expected
