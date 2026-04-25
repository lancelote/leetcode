import pytest

from src.points_that_intersect_with_cars import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([[3, 6], [1, 5], [4, 7]], 7),
        ([[1, 3], [5, 8]], 7),
    ),
)
def test_solution(nums, expected):
    assert Solution().numberOfPoints(nums) == expected
