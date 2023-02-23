import pytest

from src.baseball_game import Solution


@pytest.mark.parametrize(
    "operations,expected",
    [
        (["5", "2", "C", "D", "+"], 30),
        (["5", "-2", "4", "C", "D", "9", "+", "+"], 27),
        (["1", "C"], 0),
    ],
)
def test_solution(operations, expected):
    assert Solution().calPoints(operations) == expected
