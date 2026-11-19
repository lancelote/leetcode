import pytest

from src.shortest_word_distance import Solution


@pytest.mark.parametrize(
    "words_dict,word1,word2,expected",
    (
        (
            ["practice", "makes", "perfect", "coding", "makes"],
            "coding",
            "practice",
            3,
        ),
        (
            ["practice", "makes", "perfect", "coding", "makes"],
            "makes",
            "coding",
            1,
        ),
    ),
)
def test_solution(words_dict, word1, word2, expected):
    assert Solution().shortestDistance(words_dict, word1, word2) == expected
