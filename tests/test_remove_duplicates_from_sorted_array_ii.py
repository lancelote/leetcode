import pytest

from src.remove_duplicates_from_sorted_array_ii import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 1, 1, 2, 2, 3], 5),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
    ],
)
def test_solution(nums, expected):
    assert Solution().removeDuplicates(nums) == expected
