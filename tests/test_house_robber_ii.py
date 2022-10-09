import pytest

from src.house_robber_ii import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
        ([1], 1),
    ],
)
def test_solution(nums, expected):
    assert Solution().rob(nums) == expected
