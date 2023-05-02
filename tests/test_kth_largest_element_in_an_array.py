import pytest

from src.kth_largest_element_in_an_array import Solution


@pytest.mark.parametrize(
    "nums,k,expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
        ([1], 1, 1),
        ([2, 1], 1, 2),
    ],
)
def test_solution(nums, k, expected):
    assert Solution().findKthLargest(nums, k) == expected
