import pytest

from src.relocate_marbles import Solution


@pytest.mark.parametrize(
    "nums,move_from,move_to,expected",
    (
        ([1, 6, 7, 8], [1, 7, 2], [2, 9, 5], [5, 6, 8, 9]),
        ([1, 1, 3, 3], [1, 3], [2, 2], [2]),
    ),
)
def test_solution(nums, move_from, move_to, expected):
    assert Solution().relocateMarbles(nums, move_from, move_to) == expected
