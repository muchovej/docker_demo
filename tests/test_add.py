import pytest
from src.add import add

# test happy path
def test_addition_happy_path():
    assert add(2,3) == 5

def test_addition_negative_values():
    assert add(-2, -3) == -5

def test_addition_float():
    assert add(1.2, 2.1) == 3.3

def test_adding_one_negative_value():
    assert add(-2, 1) == -1


# Testing various happy paths (varying negative/positive values)
@pytest.mark.parametrize(
    "input1, input2, expected_value",
    [(2, 3, 5), (-2, -3, -5), (1.2, 2.1, 3.3), (-2, 1, -1)],
    )
def test_add(input1, input2, expected_value):
    assert add(input1, input2) == expected_value
