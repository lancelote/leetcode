import pytest

from src.break_a_palindrome import Solution


@pytest.mark.parametrize(
    "palindrome,expected",
    [
        ("abccba", "aaccba"),
        ("a", ""),
        ("aba", "abb"),
    ],
)
def test_solution(palindrome, expected):
    assert Solution().breakPalindrome(palindrome) == expected
