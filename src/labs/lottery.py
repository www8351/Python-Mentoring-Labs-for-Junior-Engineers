"""Lottery exercise: draw unique winning numbers and score a ticket.

The original assigned ``list.append(...)`` (which returns ``None``) to a
variable, breaking every later comparison. Here ``draw`` returns a real,
sorted, unique sample and accepts an injected RNG for deterministic tests.
"""

from __future__ import annotations

import random


def draw(
    count: int = 6,
    low: int = 1,
    high: int = 37,
    rng: random.Random | None = None,
) -> list[int]:
    """Return ``count`` unique sorted numbers drawn from ``low..high``."""
    if low > high:
        raise ValueError("low must be <= high")
    pool_size = high - low + 1
    if not 0 < count <= pool_size:
        raise ValueError("count must be between 1 and the pool size")
    generator = rng if rng is not None else random.Random()
    return sorted(generator.sample(range(low, high + 1), count))


def score(ticket: list[int], winning: list[int]) -> int:
    """Return how many of ``ticket``'s numbers appear in ``winning``."""
    return len(set(ticket) & set(winning))
