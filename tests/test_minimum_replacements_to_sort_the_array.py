import pytest

from src.minimum_replacements_to_sort_the_array import Solution


@pytest.mark.parametrize(
    "nums,expected_replacements",
    [
        ([3, 9, 3], 2),
        ([1, 2, 3, 4, 5], 0),
        ([2, 10, 20, 19, 1], 47),
    ],
)
def test_solution(nums, expected_replacements):
    assert Solution().minimumReplacement(nums) == expected_replacements
