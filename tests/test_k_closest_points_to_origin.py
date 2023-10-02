import pytest

from src.k_closest_points_to_origin import Solution


@pytest.mark.parametrize(
    "points,k,expected",
    (
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[-2, 4], [3, 3]]),
    ),
)
def test_solution(points, k, expected):
    assert Solution().kClosest(points, k) == expected
