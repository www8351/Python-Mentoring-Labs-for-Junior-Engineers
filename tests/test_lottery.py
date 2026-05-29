"""Tests for labs.lottery."""

from __future__ import annotations

import random

import pytest

from labs import lottery


def test_draw_is_deterministic_with_seed() -> None:
    first = lottery.draw(rng=random.Random(42))
    second = lottery.draw(rng=random.Random(42))
    assert first == second


def test_draw_returns_sorted_unique_in_range() -> None:
    result = lottery.draw(count=6, low=1, high=37, rng=random.Random(7))
    assert len(result) == 6
    assert len(set(result)) == 6
    assert result == sorted(result)
    assert all(1 <= n <= 37 for n in result)


def test_draw_rejects_oversized_count() -> None:
    with pytest.raises(ValueError, match="count"):
        lottery.draw(count=10, low=1, high=5)


def test_score_counts_matches() -> None:
    assert lottery.score([1, 5, 9], [5, 9, 30]) == 2
    assert lottery.score([1, 2, 3], [4, 5, 6]) == 0
