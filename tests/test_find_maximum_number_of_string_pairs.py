import pytest

from src.find_maximum_number_of_string_pairs import Solution


@pytest.mark.parametrize(
    "words,expected",
    (
        (["cd", "ac", "dc", "ca", "zz"], 2),
        (["ab", "ba", "cc"], 1),
        (["aa", "ab"], 0),
    ),
)
def test_solution(words, expected):
    assert Solution().maximumNumberOfStringPairs(words) == expected
