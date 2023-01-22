import pytest

from src.minimum_common_value import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([1, 2, 3], [2, 4], 2),
        ([1, 2, 3, 6], [2, 3, 4, 5], 2),
        ([1], [1], 1),
        ([3], [2, 3], 3),
        ([2, 3], [3], 3),
        ([1], [2], -1),
    ],
)
def test_solution(nums1, nums2, expected):
    assert Solution().getCommon(nums1, nums2) == expected
