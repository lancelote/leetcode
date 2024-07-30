import pytest

from src.jump_game_ii import Solution


@pytest.mark.parametrize(
    "nums,expected",
    (
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([2, 1], 1),
        ([1, 2, 3], 2),
    ),
)
def test_solution(nums, expected):
    assert Solution().jump(nums) == expected
