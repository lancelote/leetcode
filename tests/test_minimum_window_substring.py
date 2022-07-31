import pytest

from src.minimum_window_substring import Solution


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ABC", "D", ""),
    ],
)
def test_solution(s, t, expected):
    assert Solution().minWindow(s, t) == expected
