import pytest

from src.continuous_subarray_sum import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([23, 2, 4, 6, 7], 6, True),
        ([23, 2, 6, 4, 7], 6, True),
        ([23, 2, 6, 4, 7], 13, False),
        ([23, 2, 4, 6, 6], 7, True),
    ],
)
def test_solution(nums, k, expected):
    assert Solution().checkSubarraySum(nums, k) is expected
