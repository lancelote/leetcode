import pytest

from src.last_visited_integers import Solution


@pytest.mark.parametrize(
    "words,expected",
    (
        (["1", "2", "prev", "prev", "prev"], [2, 1, -1]),
        (["1", "prev", "2", "prev", "prev"], [1, 2, 1]),
    ),
)
def test_solution(words, expected):
    assert Solution().lastVisitedIntegers(words) == expected
