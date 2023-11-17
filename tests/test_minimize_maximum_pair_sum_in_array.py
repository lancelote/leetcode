import pytest

from src.minimize_maximum_pair_sum_in_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([3, 5, 2, 3], 7),
        ([3, 5, 4, 2, 4, 6], 8),
    ),
)
def test_solution(nums, expected):
    assert Solution().minPairSum(nums) == expected
