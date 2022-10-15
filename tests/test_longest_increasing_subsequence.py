import pytest

from src.longest_increasing_subsequence import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_solution(nums, expected):
    assert Solution().lengthOfLIS(nums) == expected
