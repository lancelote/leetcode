import pytest

from src.minimum_time_visiting_all_points import Solution


@pytest.mark.parametrize(
    "points,expected",
    [
        ([[1, 1], [3, 4], [-1, 0]], 7),
        ([[3, 2], [-2, 2]], 5),
    ],
)
def test_solution(points, expected):
    assert Solution().minTimeToVisitAllPoints(points) == expected
