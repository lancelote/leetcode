import pytest

from src.maximum_area_of_a_piece_of_cake_after_horizontal_and_vertical_cuts import (  # noqa
    Solution,
)


@pytest.mark.parametrize(
    "h,w,horizontalCuts,verticalCuts,expected_area",
    [
        (5, 4, [1, 2, 4], [1, 3], 4),
        (5, 4, [3, 1], [1], 6),
    ],
)
def test_solution(h, w, horizontalCuts, verticalCuts, expected_area):
    assert (
        Solution().maxArea(h, w, horizontalCuts, verticalCuts) == expected_area
    )
