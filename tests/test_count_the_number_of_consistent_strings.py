import pytest

from src.count_the_number_of_consistent_strings import Solution


@pytest.mark.parametrize(
    "allowed,words,expected_count",
    [
        ("ab", ["ad", "bd", "aaab", "baa", "badab"], 2),
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        ("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], 4),
    ],
)
def test_solution(allowed, words, expected_count):
    assert Solution().countConsistentStrings(allowed, words) == expected_count
