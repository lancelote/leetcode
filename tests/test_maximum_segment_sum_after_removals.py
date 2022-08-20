import pytest

from src.maximum_segment_sum_after_removals import Solution


@pytest.mark.parametrize(
    "nums,remove_indices,expected",
    [
        ([1, 2, 5, 6, 1], [0, 3, 2, 4, 1], [14, 7, 2, 2, 0]),
        ([3, 2, 11, 1], [3, 2, 1, 0], [16, 5, 3, 0]),
    ],
)
def test_solution(nums, remove_indices, expected):
    assert Solution().maximumSegmentSum(nums, remove_indices) == expected
