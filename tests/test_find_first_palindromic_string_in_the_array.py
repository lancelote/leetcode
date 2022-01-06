import pytest

from src.find_first_palindromic_string_in_the_array import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (["abc", "car", "ada", "racecar", "cool"], "ada"),
        (["notapalindrome", "racecar"], "racecar"),
        (["def", "ghi"], ""),
    ],
)
def test_solution(words, expected):
    assert Solution().firstPalindrome(words) == expected
