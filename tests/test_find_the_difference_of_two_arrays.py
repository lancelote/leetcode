import pytest

from src.find_the_difference_of_two_arrays import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    (
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ),
)
def test_solution(nums1, nums2, expected):
    assert Solution().findDifference(nums1, nums2) == expected
