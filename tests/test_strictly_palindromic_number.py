import pytest

from src.strictly_palindromic_number import is_palindrome
from src.strictly_palindromic_number import Solution


@pytest.mark.parametrize(
    "text,expected",
    [
        ([1], True),
        ([1, 2], False),
        ([1, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 2, 3, 1], False),
    ],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    "n,expected",
    [
        (9, False),
        (4, False),
    ],
)
def test_solution(n, expected):
    assert Solution().isStrictlyPalindromic(n) is expected
