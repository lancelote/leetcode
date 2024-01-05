import pytest

from src.maximum_subsequence_score import Solution


@pytest.mark.parametrize(
    "nums1,nums2,k,expected",
    (
        ([1, 3, 3, 2], [2, 1, 3, 4], 3, 12),
        ([4, 2, 3, 1, 1], [7, 5, 10, 9, 6], 1, 30),
        ([2, 1, 14, 12], [11, 7, 13, 6], 3, 168),
    ),
)
def test_solution(nums1, nums2, k, expected):
    assert Solution().maxScore(nums1, nums2, k) == expected
