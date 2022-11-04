import pytest

from src.reverse_vowels_of_a_string import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("hello", "holle"),
        ("leetcode", "leotcede"),
        ("aA", "Aa"),
    ],
)
def test_solution(s, expected):
    assert Solution().reverseVowels(s) == expected
