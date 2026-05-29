"""Text exercises: palindrome checking."""

from __future__ import annotations


def is_palindrome(value: str) -> bool:
    """Return ``True`` if ``value`` reads the same forwards and backwards.

    Case- and non-alphanumeric-insensitive, so ``"A man, a plan, a canal: Panama"``
    counts as a palindrome.
    """
    cleaned = [char.lower() for char in value if char.isalnum()]
    return cleaned == cleaned[::-1]
