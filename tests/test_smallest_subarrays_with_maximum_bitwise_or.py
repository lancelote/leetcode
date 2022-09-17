import pytest

from src.smallest_subarrays_with_maximum_bitwise_or import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 0, 2, 1, 3], [3, 3, 2, 2, 1]),
        ([1, 2], [2, 1]),
        ([4, 0, 5, 6, 3, 2], [4, 3, 2, 2, 1, 1]),
        ([0, 0, 0], [1, 1, 1]),
        ([1, 0, 0], [1, 1, 1]),
    ],
)
def test_solution(nums, expected):
    assert Solution().smallestSubarrays(nums) == expected
