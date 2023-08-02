import pytest

from src.last_stone_weight_ii import Solution


@pytest.mark.parametrize(
    "stones,expected",
    (
        ([2, 7, 4, 1, 8, 1], 1),
        ([31, 26, 33, 21, 40], 5),
    ),
)
def test_solution(stones, expected):
    assert Solution().lastStoneWeightII(stones) == expected
