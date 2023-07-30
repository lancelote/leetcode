import pytest

from src.longest_common_subsequence import Solution


@pytest.mark.parametrize(
    "text1,text2,expected",
    (
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("ee", "e", 1),
        ("bsbininm", "jmjkbkjkv", 1),
        ("mme", "em", 1),
    ),
)
def test_solution(text1, text2, expected):
    assert Solution().longestCommonSubsequence(text1, text2) == expected
