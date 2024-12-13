import pytest
import math
from operations import (
    add, subtract, multiply, divide, remainder,
    sin, cos, power, square_root, floor, ceil
)
from memory import memory_add, memory_clear, memory_recall


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (3, 5, -2),
    (0, 0, 0),
    (10, 5, 5),
    (-5, -5, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (0, 5, 0),
    (-2, 3, -6),
    (7, -8, -56),
    (-3, -3, 9),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (5, 2, 2.5),
    (-10, 2, -5),
    (7, -1, -7),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
    (5, 2, 1),
    (6, 3, 0),
    (10, 4, 2),
    (-5, 2, -1),
])
def test_remainder(a, b, expected):
    assert remainder(a, b) == expected

def test_remainder_by_zero():
    with pytest.raises(ValueError):
        remainder(1, 0)


@pytest.mark.parametrize("angle, expected", [
    (0, 0),
    (30, 0.5),
    (90, 1),
    (180, 0),
    (270, -1),
    (360, 0),
])
def test_sin(angle, expected):
    assert math.isclose(sin(angle), expected, abs_tol=1e-5)

@pytest.mark.parametrize("angle, expected", [
    (0, 1),
    (30, 0.86602540378),
    (90, 0),
    (180, -1),
    (270, 0),
    (360, 1),
])
def test_cos(angle, expected):
    assert math.isclose(cos(angle), expected, abs_tol=1e-5)


@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (5, 0, 1),
    (2, -1, 0.5),
    (3, 4, 81),
    (-2, 3, -8),
])
def test_power(base, exponent, expected):
    assert power(base, exponent) == expected


@pytest.mark.parametrize("value, expected", [
    (9, 3),
    (0, 0),
    (16, 4),
    (25, 5),
])
def test_square_root(value, expected):
    assert square_root(value) == expected

def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-1)


@pytest.mark.parametrize("value, expected", [
    (3.7, 3),
    (-3.7, -4),
    (0, 0),
    (2.0, 2),
    (-2.1, -3),
])
def test_floor(value, expected):
    assert floor(value) == expected

@pytest.mark.parametrize("value, expected", [
    (3.1, 4),
    (-3.1, -3),
    (0, 0),
    (2.0, 2),
    (-2.9, -2),
])
def test_ceil(value, expected):
    assert ceil(value) == expected


def test_memory_add_and_recall():
    memory_clear()
    memory_add(10)
    assert memory_recall() == 10
    memory_add(5)
    assert memory_recall() == 15

def test_memory_clear():
    memory_add(100)
    memory_clear()
    assert memory_recall() == 0

def test_memory_recall():
    memory_clear()
    memory_add(100)
    assert memory_recall() == 100
    memory_add(50)
    assert memory_recall() == 150
    memory_clear()
    assert memory_recall() == 0
