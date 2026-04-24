import pytest

from src.next_greater_element_i import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    (
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
    ),
)
def test_solution(nums1, nums2, expected):
    assert Solution().nextGreaterElement(nums1, nums2) == expected
