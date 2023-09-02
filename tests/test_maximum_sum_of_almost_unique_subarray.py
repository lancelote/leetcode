import pytest

from src.maximum_sum_of_almost_unique_subarray import Solution


@pytest.mark.parametrize(
    "nums,m,k,expected",
    (
        ([2, 6, 7, 3, 1, 7], 3, 4, 18),
        ([5, 9, 9, 2, 4, 5, 4], 1, 3, 23),
        ([1, 2, 1, 2, 1, 2, 1], 3, 3, 0),
        ([1], 1, 1, 1),
        ([1, 1, 1, 3], 2, 2, 4),
    ),
)
def test_solution(nums, m, k, expected):
    assert Solution().maxSum(nums, m, k) == expected
