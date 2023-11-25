import pytest

from src.sum_of_absolute_differences_in_a_sorted_array import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([2, 3, 5], [4, 3, 5]),
        ([1, 4, 6, 8, 10], [24, 15, 13, 15, 21]),
    ),
)
def test_solution(nums, expected):
    assert Solution().getSumAbsoluteDifferences(nums) == expected
