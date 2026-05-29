"""Tests for labs.text."""

from __future__ import annotations

from labs import text


def test_simple_palindrome() -> None:
    assert text.is_palindrome("racecar")


def test_palindrome_ignores_case_and_punctuation() -> None:
    assert text.is_palindrome("A man, a plan, a canal: Panama")


def test_non_palindrome() -> None:
    assert not text.is_palindrome("hello")


def test_empty_string_is_palindrome() -> None:
    assert text.is_palindrome("")
