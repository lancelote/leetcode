import pytest

from src.alien_dictionary import Solution


@pytest.mark.parametrize(
    "words,expected",
    [
        (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    ],
)
def test_solution(words, expected):
    assert Solution().alienOrder(words) == expected
