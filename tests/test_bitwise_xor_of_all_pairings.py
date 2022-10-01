import pytest

from src.bitwise_xor_of_all_pairings import Solution


@pytest.mark.parametrize(
    "nums1,nums2,expected",
    [
        ([2, 1, 3], [10, 2, 5, 0], 13),
        ([1, 2], [3, 4], 0),
    ],
)
def test_solution(nums1, nums2, expected):
    assert Solution().xorAllNums(nums1, nums2) == expected
