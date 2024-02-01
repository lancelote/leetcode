import pytest

from src.remove_duplicates_from_sorted_array_ii import Solution


@pytest.mark.parametrize(
    "nums,expected_j,expected_array",
    [
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3, 3, 3]),
    ],
)
def test_solution(nums, expected_j, expected_array):
    assert Solution().removeDuplicates(nums) == expected_j
    assert nums == expected_array
