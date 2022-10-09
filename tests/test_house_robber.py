import pytest

from src.house_robber import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([1, 2], 2),
        ([1], 1),
        ([2, 1, 1, 2], 4),
    ],
)
def test_solution(nums, expected):
    assert Solution().rob(nums) == expected
