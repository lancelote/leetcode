import pytest

from src.top_k_frequent_words import Solution


@pytest.mark.parametrize(
    "words,k,expected",
    [
        (["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]),
        (
            [
                "the",
                "day",
                "is",
                "sunny",
                "the",
                "the",
                "the",
                "sunny",
                "is",
                "is",
            ],
            4,
            ["the", "is", "sunny", "day"],
        ),
    ],
)
def test_solution(words, k, expected):
    assert Solution().topKFrequent(words, k) == expected
