import pytest
from src.running_sum_of_1d_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
    ],
)
def test_solution(nums, expected):
    assert Solution().runningSum(nums) == expected
