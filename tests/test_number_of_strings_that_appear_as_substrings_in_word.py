import pytest

from src.number_of_strings_that_appear_as_substrings_in_word import Solution


@pytest.mark.parametrize(
    "patterns,word,expected",
    [
        (["a", "abc", "bc", "d"], "abc", 3),
        (["a", "b", "c"], "aaaaabbbbb", 2),
        (["a", "a", "a"], "ab", 3),
    ],
)
def test_solution(patterns, word, expected):
    assert Solution().numOfStrings(patterns, word) == expected
