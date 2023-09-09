import pytest

from src.combination_sum_iv import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    (
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
    ),
)
def test_solution(nums, target, expected):
    assert Solution().combinationSum4(nums, target) == expected
