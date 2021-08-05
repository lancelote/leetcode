import pytest

from src.remove_duplicates_from_sorted_array import Solution


@pytest.mark.parametrize(
    "nums,unique_n,expected_arr",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ],
)
def test_solution(nums, unique_n, expected_arr):
    assert Solution().removeDuplicates(nums) == unique_n
    assert nums[:unique_n] == expected_arr
