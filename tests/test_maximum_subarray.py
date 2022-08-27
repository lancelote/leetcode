import pytest

from src.maximum_subarray import Solution


@pytest.mark.parametrize(
    "nums,expected_sub",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-3, -2, -1], -1),
    ],
)
def test_solution(nums, expected_sub):
    assert Solution().maxSubArray(nums) == expected_sub
