import pytest

from src.find_all_anagrams_in_a_string import Solution


@pytest.mark.parametrize(
    "s,p,expected",
    [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("", "ab", []),
    ],
)
def test_solution(s, p, expected):
    assert Solution().findAnagrams(s, p) == expected
