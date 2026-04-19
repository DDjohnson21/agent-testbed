import pytest

from testbed.mathutils import add, multiply, is_even, sum_range


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    # Issue: add returns a - b for negative numbers.
    assert add(-2, -3) == -5


def test_multiply_basic():
    # Issue: multiply is not implemented.
    assert multiply(3, 4) == 12


def test_multiply_zero():
    assert multiply(0, 99) == 0


def test_is_even_positive():
    assert is_even(4) is True
    assert is_even(5) is False


def test_is_even_negative():
    # Issue: is_even fails for negative odd numbers in some implementations.
    assert is_even(-3) is False
    assert is_even(-4) is True


def test_sum_range_inclusive():
    # Issue: sum_range should be inclusive of end (off-by-one).
    assert sum_range(1, 5) == 1 + 2 + 3 + 4 + 5
