import pytest

from src.valid_palindrome import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("aa", True),
        (".,", True),
    ],
)
def test_solution(s, expected):
    assert Solution().isPalindrome(s) == expected
