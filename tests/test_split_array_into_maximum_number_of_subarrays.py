import pytest

from src.split_array_into_maximum_number_of_subarrays import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([1, 0, 2, 0, 1, 2], 3),
        ([5, 7, 1, 3], 1),
        ([0, 8, 0, 0, 0, 23], 4),
    ),
)
def test_solution(nums, expected):
    assert Solution().maxSubarrays(nums) == expected
