import pytest

from src.target_sum import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        ([1, 1, 1, 1, 1], 3, 5),
        ([1], 1, 1),
        ([1, 1, 1], 1, 3),
    ),
)
def test_solution(nums, target, expected):
    assert Solution().findTargetSumWays(nums, target) == expected
