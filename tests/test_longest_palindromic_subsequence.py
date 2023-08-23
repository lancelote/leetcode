import pytest

from src.longest_palindromic_subsequence import Solution


@pytest.mark.parametrize(
    "s,expected",
    (
        ("bbbab", 4),
        ("cbbd", 2),
    ),
)
def test_solution(s, expected):
    assert Solution().longestPalindromeSubseq(s) == expected
