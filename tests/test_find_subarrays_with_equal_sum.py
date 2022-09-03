import pytest

from src.find_subarrays_with_equal_sum import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([4, 2, 4], True),
        ([1, 2, 3, 4, 5], False),
        ([0, 0, 0], True),
    ],
)
def test_solution(nums, expected):
    assert Solution().findSubarrays(nums) is expected
