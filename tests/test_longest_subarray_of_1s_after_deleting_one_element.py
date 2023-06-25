import pytest

from src.longest_subarray_of_1s_after_deleting_one_element import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 1, 0, 1], 3),
        ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
        ([1, 1, 1], 2),
    ),
)
def test_solution(nums, expected):
    assert Solution().longestSubarray(nums) == expected
