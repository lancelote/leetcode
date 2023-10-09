import pytest

from src.find_first_and_last_position_of_element_in_sorted_array import (
    Solution,
)


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
        ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
        ([], 0, [-1, -1]),
        ([1], 1, [0, 0]),
        ([1, 3], 1, [0, 0]),
    ),
)
def test_solution(nums, target, expected):
    assert Solution().searchRange(nums, target) == expected
