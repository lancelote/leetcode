import pytest

from src.valid_palindrome_ii import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("aba", True),
        ("abca", True),
        ("abc", False),
    ],
)
def test_solution(s, expected):
    assert Solution().validPalindrome(s) == expected
