import pytest

from src.max_dot_product_of_two_subsequences import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    (
        ([2, 1, -2, 5], [3, 0, -6], 18),
        ([3, -2], [2, -6, 7], 21),
        ([-1, -1], [1, 1], -1),
    ),
)
def test_solution(nums1, nums2, expected):
    assert Solution().maxDotProduct(nums1, nums2) == expected
