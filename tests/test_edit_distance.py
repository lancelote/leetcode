import pytest

from src.edit_distance import Solution


@pytest.mark.parametrize(
    "word1,word2,expected",
    (
        ("horse", "ros", 3),
        ("intention", "execution", 5),
    ),
)
def test_solution(word1, word2, expected):
    assert Solution().minDistance(word1, word2) == expected
