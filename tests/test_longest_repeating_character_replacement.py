import pytest

from src.longest_repeating_character_replacement import Solution


@pytest.mark.parametrize(
    "s,k,expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
    ],
)
def test_solution(s, k, expected):
    assert Solution().characterReplacement(s, k) == expected
