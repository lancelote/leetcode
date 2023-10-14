import pytest

from src.painting_the_walls import Solution


@pytest.mark.parametrize(
    "cost,time,expected",
    (
        ([1, 2, 3, 2], [1, 2, 3, 2], 3),
        ([2, 3, 4, 2], [1, 1, 1, 1], 4),
    ),
)
def test_solution(cost, time, expected):
    assert Solution().paintWalls(cost, time) == expected
