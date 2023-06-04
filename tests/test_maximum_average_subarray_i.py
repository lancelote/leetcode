import pytest

from src.maximum_average_subarray_i import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    (
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
    ),
)
def test_solution(nums, k, expected):
    assert Solution().findMaxAverage(nums, k) == expected
