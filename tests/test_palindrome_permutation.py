import pytest

from src.palindrome_permutation import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("code", False),
        ("aab", True),
        ("carerac", True),
    ),
)
def test_solution(s, expected):
    assert Solution().canPermutePalindrome(s) is expected
