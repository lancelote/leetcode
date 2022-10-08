import pytest

from src._3sum_closest import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
    ],
)
def test_solution(nums, target, expected):
    assert Solution().threeSumClosest(nums, target) == expected
