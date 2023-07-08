import pytest

from src.longest_alternating_subarray import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([2, 3, 4, 3, 4], 4),
        ([4, 5, 6], 2),
        ([21, 9, 5], -1),
    ),
)
def test_solution(nums, expected):
    assert Solution().alternatingSubarray(nums) == expected
