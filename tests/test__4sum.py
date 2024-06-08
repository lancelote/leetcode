import pytest

from src._4sum import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        (
            [1, 0, -1, 0, -2, 2],
            0,
            [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        ),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ),
)
def test_solution(nums, target, expected):
    assert Solution().fourSum(nums, target) == expected
