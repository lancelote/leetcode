import pytest

from src.palindromic_substrings import Solution


@pytest.mark.parametrize(
    "s,expected_count",
    [
        ("abc", 3),
        ("aaa", 6),
    ],
)
def test_solution(s, expected_count):
    assert Solution().countSubstrings(s) == expected_count
