from programs.calculator import add, substract, multiply, division
from pytest import mark


@mark.parametrize("x, y, expected_result", [
    (3, 4, 7),
    (4, 8, 12),
    (2, 10, 12)
])
def test_add_function(x, y, expected_result):
    assert add(x, y) == expected_result



@mark.parametrize("x, y, expected_result", [
    (20, 4, 16),
    (10, 2, 8),
    (8, 20, -12)
])
def test_substract_function(x, y, expected_result):
    assert substract(x, y) == expected_result


def test_multiply_function():
    assert multiply(2, 3) == 6


def test_division_function():
    assert division(6, 2) == 3