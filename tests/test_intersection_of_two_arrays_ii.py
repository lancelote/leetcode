from collections import Counter

import pytest

from src.intersection_of_two_arrays_ii import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    (
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
    ),
)
def test_solution(nums1, nums2, expected):
    result = Solution().intersect(nums1, nums2)

    assert Counter(result) == Counter(expected)
