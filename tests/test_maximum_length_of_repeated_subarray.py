import pytest

from src.maximum_length_of_repeated_subarray import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
    ],
)
def test_solution(nums1, nums2, expected):
    assert Solution().findLength(nums1, nums2) == expected
