import pytest

from src.unique_length_3_palindromic_subsequences import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("aabca", 3),
        ("adc", 0),
        ("bbcbaba", 4),
        ("ckafnafqo", 4),
    ),
)
def test_solution(s, expected):
    assert Solution().countPalindromicSubsequence(s) == expected
