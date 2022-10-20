import pytest

from src.jump_game import Solution


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
    ],
)
def test_solution(nums, expected):
    assert Solution().canJump(nums) == expected
