"""Arithmetic exercises: multiplication tables, digit extraction, Fibonacci."""

from __future__ import annotations


def multiplication_table(n: int, up_to: int = 10) -> list[tuple[int, int, int]]:
    """Return ``(n, i, n * i)`` rows for ``i`` in ``1..up_to``."""
    if up_to < 1:
        raise ValueError("up_to must be >= 1")
    return [(n, i, n * i) for i in range(1, up_to + 1)]


def extract_digits(number: int) -> list[int]:
    """Return the base-10 digits of ``number``, most significant first."""
    n = abs(number)
    if n == 0:
        return [0]
    digits: list[int] = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits[::-1]


def fibonacci(n: int) -> int:
    """Return the ``n``-th Fibonacci number (``fib(0) == 0``, ``fib(1) == 1``).

    Iterative, so small ``n`` like 0 and 1 never index an empty sequence
    (the original script crashed on ``seq[i - 1]`` when ``i < 2``).
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def is_valid_fibonacci(value: int) -> bool:
    """Return ``True`` if ``value`` is a Fibonacci number."""
    if value < 0:
        return False
    a, b = 0, 1
    while a < value:
        a, b = b, a + b
    return a == value
