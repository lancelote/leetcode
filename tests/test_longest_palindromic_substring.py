import pytest

from src.longest_palindromic_substring import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
    ],
)
def test_solution(s, expected):
    assert Solution().longestPalindrome(s) == expected
