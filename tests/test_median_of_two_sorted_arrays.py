import pytest

from src.median_of_two_sorted_arrays import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    (
        ([1, 3], [2], 2),
        ([1, 2], [3, 4], 2.5),
        ([], [], 0),
        ([1], [], 1),
        ([], [1], 1),
    ),
)
def test_solution(nums1, nums2, expected):
    assert Solution().findMedianSortedArrays(nums1, nums2) == expected
