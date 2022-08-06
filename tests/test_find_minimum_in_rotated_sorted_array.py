import pytest

from src.find_minimum_in_rotated_sorted_array import Solution


@pytest.mark.parametrize(
    "nums,expected_min",
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        ([1], 1),
        ([2, 1], 1),
    ],
)
def test_solution(nums, expected_min):
    assert Solution().findMin(nums) == expected_min
