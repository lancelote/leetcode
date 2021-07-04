import pytest

from src.sum_of_all_subset_xor_totals import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 3], 6),
        ([5, 1, 6], 28),
        ([3, 4, 5, 6, 7, 8], 480),
    ],
)
def test_solution(nums, expected):
    assert Solution().subsetXORSum(nums) == expected
