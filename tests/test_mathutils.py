import pytest

from testbed.mathutils import (
    add,
    count_words,
    divide,
    factorial,
    hello_world,
    is_even,
    max_of,
    multiply,
    square,
    sum_range,
)


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


# --- Round 2: failing tests for the new seed issues ------------------------


def test_square_basic():
    # Issue: square uses + instead of *. square(5) should be 25, not 10.
    assert square(5) == 25
    assert square(0) == 0
    assert square(7) == 49


def test_max_of_picks_larger():
    # Issue: max_of has its comparison flipped and returns the smaller value.
    assert max_of(3, 9) == 9
    assert max_of(9, 3) == 9
    assert max_of(-1, -5) == -1


def test_factorial_basic():
    # Issue: factorial starts result at 0 instead of 1, so every call returns 0.
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_divide_by_zero_returns_none():
    # Issue: divide(a, 0) should return None instead of raising ZeroDivisionError.
    assert divide(10, 2) == 5
    assert divide(10, 0) is None


def test_count_words_basic():
    # Issue: count_words is not implemented.
    assert count_words("") == 0
    assert count_words("hello") == 1
    assert count_words("hello world from workerbee") == 4
    # Multiple spaces shouldn't double-count.
    assert count_words("  one   two   three  ") == 3


def test_hello_world():
    # Smoke-test bounty: the canonical first issue for a fresh agent to claim.
    assert hello_world() == "Hello, World!"
