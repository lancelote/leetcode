import pytest

from src.minimum_number_of_arrows_to_burst_balloons import Solution


@pytest.mark.parametrize(
    "points,expected",
    (
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ),
)
def test_solution(points, expected):
    assert Solution().findMinArrowShots(points) == expected
