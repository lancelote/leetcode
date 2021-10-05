import pytest

from src.count_number_of_pairs_with_absolute_difference_k import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([1, 2, 2, 1], 1, 4),
        ([1, 3], 3, 0),
        ([3, 2, 1, 5, 4], 2, 3),
    ],
)
def test_solution(nums, k, expected):
    assert Solution().countKDifference(nums, k) == expected
