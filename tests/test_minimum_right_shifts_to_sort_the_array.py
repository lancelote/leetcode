import pytest

from src.minimum_right_shifts_to_sort_the_array import Solution


@pytest.mark.parametrize(
    "nums, expected",
    (
        ([3, 4, 5, 1, 2], 2),
        ([1, 3, 5], 0),
        ([2, 1, 4], -1),
    ),
)
def test_solution(nums, expected):
    assert Solution().minimumRightShifts(nums) == expected
