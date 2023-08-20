import pytest

from src.shortest_common_supersequence import lcs
from src.shortest_common_supersequence import Solution


@pytest.mark.parametrize(
    "str1,str2,expected",
    (
        ("abcde", "ace", "ace"),
        ("abc", "abc", "abc"),
        ("abc", "def", ""),
    ),
)
def test_lcs(str1, str2, expected):
    assert lcs(str1, str2) == expected


@pytest.mark.parametrize(
    "str1,str2,expected",
    (
        ("abac", "cab", "cabac"),
        ("aaaaaaaa", "aaaaaaaa", "aaaaaaaa"),
    ),
)
def test_solution(str1, str2, expected):
    assert Solution().shortestCommonSupersequence(str1, str2) == expected
