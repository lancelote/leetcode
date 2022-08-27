import pytest

from src.largest_rectangle_in_histogram import Solution


@pytest.mark.parametrize(
    "heights,expected_area",
    [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1], 1),
        ([1, 1], 2),
        ([3, 6, 5, 7, 4, 8, 1, 0], 20),
    ],
)
def test_solution(heights, expected_area):
    assert Solution().largestRectangleArea(heights) == expected_area
