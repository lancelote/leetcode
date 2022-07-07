import pytest

from src._3sum import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        # ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        # ([0, 1, 1], []),
        # ([0, 0, 0], [[0, 0, 0]]),
        # ([-3, 1, 1, 1, 2], [[-3, 1, 2]]),
        ([1, -1, -1, 0], [[-1, 0, 1]])
    ],
)
def test_solution(nums, expected):
    assert Solution().threeSum(nums) == expected
