import pytest

from src.merge_strings_alternately import Solution


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    ],
)
def test_solution(word1, word2, expected):
    assert Solution().mergeAlternately(word1, word2) == expected
