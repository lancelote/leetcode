import pytest

from src.maximum_number_of_vowels_in_a_substring_of_given_length import (
    Solution,
)


@pytest.mark.parametrize(
    "s,k,expected",
    (
        ("abciiidef", 3, 3),
        ("aeiou", 2, 2),
        ("leetcode", 3, 2),
        ("weallloveyou", 7, 4),
    ),
)
def test_solution(s, k, expected):
    assert Solution().maxVowels(s, k) == expected
