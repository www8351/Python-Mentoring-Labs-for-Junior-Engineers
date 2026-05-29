"""Tests for labs.arithmetic."""

from __future__ import annotations

import pytest

from labs import arithmetic


def test_multiplication_table() -> None:
    assert arithmetic.multiplication_table(3, up_to=3) == [(3, 1, 3), (3, 2, 6), (3, 3, 9)]


def test_multiplication_table_rejects_bad_bound() -> None:
    with pytest.raises(ValueError, match="up_to"):
        arithmetic.multiplication_table(3, up_to=0)


def test_extract_digits() -> None:
    assert arithmetic.extract_digits(1234) == [1, 2, 3, 4]
    assert arithmetic.extract_digits(0) == [0]
    assert arithmetic.extract_digits(-57) == [5, 7]


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 0), (1, 1), (2, 1), (7, 13), (10, 55)],
)
def test_fibonacci(n: int, expected: int) -> None:
    assert arithmetic.fibonacci(n) == expected


def test_fibonacci_rejects_negative() -> None:
    with pytest.raises(ValueError, match="n must be"):
        arithmetic.fibonacci(-1)


def test_is_valid_fibonacci() -> None:
    assert arithmetic.is_valid_fibonacci(13)
    assert not arithmetic.is_valid_fibonacci(14)
    assert not arithmetic.is_valid_fibonacci(-1)
