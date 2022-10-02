import pytest

from src.number_of_dice_rolls_with_target_sum import Solution


@pytest.mark.parametrize(
    "n,k,target,expected",
    [
        (1, 6, 3, 1),
        (2, 6, 7, 6),
        (30, 30, 500, 222616187),
    ],
)
def test_solution(n, k, target, expected):
    assert Solution().numRollsToTarget(n, k, target) == expected
